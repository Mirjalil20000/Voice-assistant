import speech_recognition as sr
from gtts import gTTS
import playsound
import os
import requests
import yfinance as yf
import wolframalpha
import translators as ts
import wikipedia
import datetime

#crytocurrency api 
crypto_api = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin%2Clitecoin%2Csolana&vs_currencies=usd'

#WolframAlpha API key
wolfram_api = '48T9YL-QAGETGAQ6T'

# Chuck_Norris API

chuck_norris_api = 'https://api.chucknorris.io/jokes/random'

# News API Key
news_api_key = '86621ad97dbf4968ad039bcdb121b668'

# Weather API Key
weather_api_key = '1663a9eb7b38413b91ae913602dc9d47'



#Capital of country
def wolfram_alpha_country_capital(text):
    client = wolframalpha.Client(wolfram_api)
    result = client.query(text)
    answer = next(result.results).text
    answer_split = answer.split()
    capital_result = 'The capital of ' + answer_split[-1] + ' ' + 'is' + ' ' + answer_split[0] 
    print(capital_result)
    alina_talk(capital_result)
    
#Calculator    
def wolfram_alpha_calculator(text):
    client = wolframalpha.Client(wolfram_api)
    result = client.query(text)
    answer = next(result.results).text
    print(answer)
    alina_talk('The answer is ' + answer)


#President

def wolfram_alpha_president(text):
    client = wolframalpha.Client(wolfram_api)
    result = client.query(text)
    answer = next(result.results).text
    print(answer)
    alina_talk('The president is ' + answer)
    
    
#Translator

def translator(text):
    alina_talk_ru(ts.google(text, from_language='en', to_language='ru'))

    
def chuck_norris():
    cn_data = requests.get(chuck_norris_api)
    cn_json = cn_data.json()
    joke = (cn_json['value'])
    print(joke)
    alina_talk(joke)
    


def get_news():
    news_url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=' + news_api_key
    news = requests.get(news_url).json()
    articles = news['articles']
    
    news_headlines = []
    for art in articles:
        news_headlines.append(art['title'])

    for i in range(3):
        print(news_headlines[i])
        alina_talk((news_headlines[i]))
        
def get_weather():
    alina_talk('No Problem, I will look it up for you. What city are you interested in?')
    weather_input = alina_listen()
    print(weather_input)
    
    weather_url = 'https://api.weatherbit.io/v2.0/current?city=' + weather_input + '&key=' + weather_api_key
    weather = requests.get(weather_url).json()
    temperature = weather['data'][0]['temp']
    description = weather['data'][0]['weather']['description']
    weather_result = 'The temperature ' + weather_input + ' is ' + str(temperature) + ' degrees and you can see ' + description
    #print(weather_result)
    alina_talk(weather_result)
    
    
def wikipedia_info():
    alina_talk("I'm happy to help you. Let me know what should I search for you on Wikipedia?")
    wiki_listen = alina_listen()
    wiki_result = wikipedia.summary(wiki_listen, sentences=1)
    print(wiki_result)
    alina_talk(wiki_result)



def time_now():
            today_date = datetime.datetime.now()
            hour = today_date.strftime("%I")
            minute = today_date.strftime("%M")
            meridiem = today_date.strftime("%p") 
            time_now = 'It is ' + hour + ':' + minute + ' ' + meridiem
            print(time_now)
            alina_talk(time_now)
def weekday_now():
           weekday_today = datetime.datetime.now().strftime("%A")
           print(weekday_today)
           alina_talk(weekday_today)




# Convert speech to test so we can use the text for the next step
def alina_listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        text = ''
        
        try:
            text = r.recognize_google(audio)
            
        except sr.RequestError as re:
            print(re)
            
        except sr.UnknownValueError as uve:
            print(uve)
            
        except sr.WaitTimeoutError as wte:
            print(wte)
            
    text = text.lower()
    return text
            
# Convert text to speech
def alina_talk(text):
    file_name = 'audio_data.mp3'
    tts = gTTS(text=text, lang='en')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
    
    
# Convert text to speech Russian    
def alina_talk_ru(text):
    file_name = 'audio_data.mp3'
    tts = gTTS(text=text, lang='ru')
    tts.save(file_name)
    playsound.playsound(file_name)
    os.remove(file_name)
        

    
    
    
    
# Create a function which will give us back a reply based on the input text    
def alina_reply(text):
    if 'what' in text and 'name' in text:
        alina_talk('My name is Alina, and I am your personal assistant')
    
    elif  'why' in text and 'exist' in text:
        alina_talk('I was created to work you. I dont need break, and I will never ask days off')
    
    elif 'when' in text and 'sleep' in text:
        alina_talk('I never sleep, I was created to support 24 hours')
        
    elif 'you' in text and 'stupid' in text:
        alina_talk('No I am not stupid. My grandmother told me that there are no stupid persons there.'
                   + 'I try to give my best everyday and learn continuously')
        
    elif 'favourite' in text or 'favorite' in text and 'movie' in text:
        alina_talk('My favourite movie is Harry Potter. I watch it with my friends all the time')
    
    #crytocurrency information - #Bitcoin
    elif 'bitcoin' in text:
       response = requests.get(crypto_api)
       crypto_json = response.json()
       alina_talk('The current price of Bitcoin is' + str(crypto_json['bitcoin']['usd']) +' US Dollars')
       
   #crytocurrency information - #Solana
    elif 'solana' in text:
       response = requests.get(crypto_api)
       crypto_json = response.json()
       alina_talk('The current price of Solana is' + str(crypto_json['solana']['usd']) +' US Dollars') 
    
    
   #crytocurrency information - #Litecoin
    elif 'litecoin' in text:
       response = requests.get(crypto_api)
       crypto_json = response.json()
       alina_talk('The current price of Litecoin is' + str(crypto_json['litecoin']['usd']) +' US Dollars') 
    
    #Stock Market Information -Apple
    elif 'apple' in text:
        apple = yf.Ticker('AAPL')
        print(apple.info['regularMarketPrice'])
        alina_talk('At this moment you can buy one Apple share for ' + str(apple.info['regularMarketPrice']) + ' US Dollars')  


    #Stock Market Information - Facebook
    elif 'facebook' in text:
        facebook = yf.Ticker('FB')
        print(facebook.info['regularMarketPrice'])
        alina_talk('At this moment you can buy one Facebook share for ' + str(facebook.info['regularMarketPrice']) + ' US Dollars') 
        
        
    #Stock Market Information - Tesla
    elif 'tesla' in text:
        tesla = yf.Ticker('TSLA')
        print(tesla.info['regularMarketPrice'])
        alina_talk('At this moment you can buy one Tesla share for ' + str(tesla.info['regularMarketPrice']) + ' US Dollars') 


    #Stock Market Information - Google
    elif 'google' in text:
        google = yf.Ticker('GOOG')
        print(google.info['regularMarketPrice'])
        alina_talk('At this moment you can buy one Google share for ' + str(google.info['regularMarketPrice']) + ' US Dollars') 


    #Stock Market Information - Amazon
    elif 'amazon' in text:
        amazon = yf.Ticker('AMZN')
        print(amazon.info['regularMarketPrice'])
        alina_talk('At this moment you can buy one Amazon share for ' + str(amazon.info['regularMarketPrice']) + ' US Dollars') 

    
    #Wolfram Alpha - Capital of country
    elif 'capital' in text and 'of' in text:
        wolfram_alpha_country_capital(text)

    
    #Wolfram Alpha Calculator
    elif  '+' in text or '-' in text or 'multiply' in text or 'multipled' in text or 'divide' in text or 'root' in text:
        wolfram_alpha_calculator(text)


    #Wolfram Alpha President
    elif 'who' in text and 'president' in text:
        wolfram_alpha_president(text)
    
    
    #Translator
    elif 'translate' in text:
        alina_talk('Sure, what do you need me to translate')
        while True:
             text_to_translate = alina_listen()
             if text_to_translate != 'turn off translator':
                 translator(text_to_translate)   
             else:
                 alina_talk('The translator will be turned off.. What else can I do for you?')
                 break
             
    # Chuck Norris jokes
    elif 'chuck norris' in text:     
            chuck_norris()
            
      # Top 3 news headlines  
    elif 'news' in text:
         alina_talk('Alright, let me tell you the first three headlines')
         get_news()
        
    # Weather information
    elif 'weather' in text:
        get_weather()
        
        
    # Wikipedia
    elif 'wikipedia' in text:
        wikipedia_info()
    
    
    
    elif 'stop' in text:
        alina_talk('It was pleasure to help you, I wish you a wonderful day') 
        
    else:
        alina_talk('Excuse me, I did not get that, can you repeat it?')
        
def execute_assistant():
    #personalize name
    alina_talk('Hi, I am here to support you. Can you tell me your name')
    listen_name = alina_listen()
    alina_talk('Hi ' + listen_name + 'what can I do for you')
    while True:
        listen_alina = alina_listen()
        print(listen_alina)
        alina_reply(listen_alina)
        
        
        if 'stop' in listen_alina:
            break

execute_assistant()









        