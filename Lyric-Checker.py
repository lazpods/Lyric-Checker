from better_profanity import profanity
from lyricsgenius import Genius

# Initialize the profanity filter
profanity.load_censor_words()

# Initialize the Genius API
genius = Genius('FNwup5QIwPws1x76qmMZp57uESOY2YnNZOefk7zwS_jWTIJA5fNK2R2e_wkSK6iZ')

# Search for the song using inputs
song_title = input("Enter song title: ")
song_artist = input("Enter song artist: ")

# Get the lyrics for the song
song = genius.search_song(song_title, artist=song_artist)

