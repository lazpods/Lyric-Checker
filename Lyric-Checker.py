from better_profanity import profanity
import requests

# Initialize the profanity filter
profanity.load_censor_words()

# Replace YOUR_ACCESS_TOKEN with your actual access token
headers = {'Authorization': 'Bearer YHvbmVbaCWQ35JNuwADK2aazsbJs6iX--fMy_OTrZBSxGLCq6Hu7rG0E-bOcgoWA'}

# Replace SONG_NAME and ARTIST_NAME with the name of the song and artist you want to search for
song_name = input("Enter desired song name: ")
artist_name = input("Enter artist of desired song: ")
query = f"{song_name} {artist_name}"
response = requests.get(f'https://api.genius.com/search?q={query}', headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Get the lyrics from the response
    lyrics = response.json()['response']['song']['lyrics']

    # Write the lyrics to a text file
    with open('lyrics.txt', 'w') as file:
        file.write(lyrics)
else:
    print("Request failed with status code:", response.status_code)


def explicitCheck():
    # Read the text file into a string
    with open('lyrics.text', 'r') as file:
        text = file.read()

    # Check if the text contains any profanity
    if profanity.contains_profanity(text):
        print("Warning: This text contains profanity.")
        text.close()
    else:
        print("The text is clean.")
        text.close()



