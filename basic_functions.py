#  Copyright (c) 2023 - James C. Burchill
#  File Location: ~/eleven_labs/basic_functions.py
#  Last Updated: 2023-04-07

import os
import sys
import tempfile

import requests
from dotenv import load_dotenv

hasAPIKey = False  # Set to True if you have an API key
eleven_labs_api_key = None
notUsed = None


def get_voices():
    if not hasAPIKey:
        sys.exit("You need an API key to use this function.")
    # Create the headers
    _headers = {"xi-api-key": eleven_labs_api_key}
    # Create the URL
    url = "https://api.elevenlabs.io/v1/voices"
    # Send the request
    response = requests.get(url, headers=_headers)
    # Check for errors
    response.raise_for_status()
    # Return the JSON
    return response.json()


def speak(text, v_id):
    if not hasAPIKey:
        sys.exit("You need an API key to use this function.")
    # Create the headers
    _headers = {"xi-api-key": eleven_labs_api_key}
    # Create the URL
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{v_id}"
    # Send the request
    response = requests.post(url, headers=_headers, json={"text": text})
    # Check for errors
    response.raise_for_status()
    play_audio(response.content)


def play_audio(c):
    # Now save the audio to a temp file and play it (file auto deletes when exiting 'with')
    with tempfile.NamedTemporaryFile(suffix=".wav") as f:
        f.write(c)
        os.system(f"afplay {f.name}")


def demo_voices():
    if not hasAPIKey:
        sys.exit("You need an API key to use this function.")
    # Get the voices
    voices = get_voices()
    s = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
    # Speak with each voice
    for v in voices['voices']:
        print(f"Voice: {v['name']} ID: {v['voice_id']}")
        speak(f"Hello, I'm {v['name']}. {s}", v['voice_id'])


def input_voice():
    if not hasAPIKey:
        sys.exit("You need an API key to use this function.")
    # Get the voices
    voices = get_voices()
    # Speak with each voice
    for v in voices['voices']:
        print(v['name'])
    # Ask the user to choose a voice
    name = input('What voice do you want to use? (Press Enter to continue)')
    v_id = None
    # Find the voice
    for v in voices['voices']:
        if v['name'] == name:
            v_id = v['voice_id']
            break
    # Return the voice ID and name
    return v_id, v['name']


def list_voices():
    if not hasAPIKey:
        sys.exit("You need an API key to use this function.")
    # Get the voices
    voices = get_voices()
    # List each voice
    return [v['name'] for v in voices['voices']]


def select_voice(x):
    if not hasAPIKey:
        sys.exit("You need an API key to use this function.")
    # Get the voices
    voices = get_voices()
    # Find the voice
    for v in voices['voices']:
        if v['name'] == x:
            break
    # Return the voice ID and name
    return v['voice_id'], v['name']


def get_eleven_labs_api_key():
    global hasAPIKey, eleven_labs_api_key
    try:
        load_dotenv()  # Load all the ENV variables into your os enviroment.
        eleven_labs_api_key = os.getenv("ELEVEN_LABS_API_KEY")  # Get your API key from an environment variable
        hasAPIKey = True
    except Exception as e:
        sys.exit("Unable to get the OpenAI API key")


if __name__ == "__main__":

    get_eleven_labs_api_key()

    answer = input("Would you like to hear the voices? (y/n) ")
    if answer == "y":
        demo_voices()
    else:
        sys.exit("OK, goodbye.")
