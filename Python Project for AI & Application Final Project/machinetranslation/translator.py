import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

# translate en to fr
def english_to_french(english_text):
    '''translate en to fr'''
    
    french_text = language_translator.translate(
                text=english_text,
                model_id='en-fr').get_result()
    #print(json.dumps(frenchText, indent=2, ensure_ascii=False))
    return french_text#

def french_to_english(french_text):
    '''translate fr to en'''
    english_text = language_translator.translate(
                text=french_text,
                model_id='fr-en').get_result()
    (json.dumps(english_text, indent=2, ensure_ascii=False))
    return english_text
#print(englishToFrench('Hello')['translations'][0]['translation'])
#frenchToEnglish(None)
