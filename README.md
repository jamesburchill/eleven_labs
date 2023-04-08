# eleven_labs (Basic Functions)

## Important

You need an ELEVEN LABS API. 

You can get one here: https://elevenlabs.io

You also need a `.env` file in the project. This file must contain the following line (which it the API key):

`ELEVEN_LABS_API_KEY=XXXXXXXXXXXXXX`

## Installation

Just copy the file in your project and ensure you install the required packages

## Requirements

```
    requests~=2.28.2
    python-dotenv~=1.0.0
```

## Usage

Simply run the script and you can hear the main voices. 

Check out the various functions to see just how easy it easy to use.

## Example.py

```
    import eleven_labs as el

    el.get_eleven_labs_api_key()  # Required to get the API key from the .env file
     
    el.list_voices()  # entirely optional, lists all the voices available
    
    v = el.select_voice('Adam')  # set the voice to Adam
    
    el.speak(v, 'Hello World')  # have Adam say 'Hello World'
    
```

## Notes

This app was designed to run on a Mac. It uses the `afplay` command to play the audio file. If this is not available on your system, you will need to change the `play_audio` function to use a different command.
