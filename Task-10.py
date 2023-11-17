#1.using the python pip command create a "requirements.txt" file from the terminal/command prompt

 #using freeze command -install requirements.txt

#          pip freeze > requirements.txt

'''se the pip freeze command to generate a requirements.txt file from the command prompt.
This command will list all the installed packages and their versions in the
currently active Python environment. '''


#2.using python pip command istall flask module<2.0

#         pip install flask ==version # used to install specific version

#         pip install flask <2.0      # install <2.0 version 

#3.
'''Create a music player web app using html, oops, typescript and bootstrap with the following features.

Users can create audio using URLs available online.
Users can create multiple Playlists based on the genre of the song.
Users can add multiple audio files into each playlist created.
Users can search audio by name.
Users can search the playlist by name.
Users can give ratings to playlist and audio. Rating displayed is the average rating calculated after each submission.
For displaying Average rating:
Create 3 users and randomly generate ratings from 1 to 5.
find the average rating from the random number generated and display it in the front end.
Audio player customization feature will fetch additional points.
'''

import random

class Audio:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.ratings = []

    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)

    def calculate_average_rating(self):
        return sum(self.ratings) / len(self.ratings) if self.ratings else 0

class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.audios = []
        self.ratings = []

    def add_audio(self, audio):
        self.audios.append(audio)

    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)

    def calculate_average_rating(self):
        return sum(self.ratings) / len(self.ratings) if self.ratings else 0

class User:
    def __init__(self, name):
        self.name = name

    def rate_audio(self, audio, rating):
        audio.add_rating(rating)

    def rate_playlist(self, playlist, rating):
        playlist.add_rating(rating)

class MusicPlayer:
    def __init__(self):
        self.users = []
        self.playlists = []

    def create_user(self, name):
        user = User(name)
        self.users.append(user)
        return user

    def create_playlist(self, name, genre):
        playlist = Playlist(name, genre)
        self.playlists.append(playlist)
        return playlist
    def search_audio_by_name(self, name):
        # Implement audio search logic by name
        pass
    def search_Playlist_by_name(self, name):
        # Implement audio search logic by name
        pass


# Example usage:
player = MusicPlayer()

# Creating users
user1 = player.create_user("Alice")
user2 = player.create_user("Bob")
user3 = player.create_user("Charlie")

# Creating playlists
playlist1 = player.create_playlist("Pop Hits", "Pop")
playlist2 = player.create_playlist("Rock Classics", "Rock")

# Adding audio to playlists
audio1 = Audio("Song 1", "https://example.com/song1.mp3")
audio2 = Audio("Song 2", "https://example.com/song2.mp3")
audio3 = Audio("Song 3", "https://example.com/song3.mp3")

playlist1.add_audio(audio1)
playlist1.add_audio(audio2)
playlist2.add_audio(audio3)

# Users rating audios and playlists
user1.rate_audio(audio1, random.randint(1, 5))
user2.rate_audio(audio1, random.randint(1, 5))
user3.rate_audio(audio2, random.randint(1, 5))

user1.rate_playlist(playlist1, random.randint(1, 5))
user2.rate_playlist(playlist1, random.randint(1, 5))
user3.rate_playlist(playlist2, random.randint(1, 5))

# Calculating average ratings
average_rating_playlist1 = playlist1.calculate_average_rating()
average_rating_audio1 = audio1.calculate_average_rating()

print(f"Average rating for Playlist 1: {average_rating_playlist1}")
print(f"Average rating for Audio 1: {average_rating_audio1}")


'''
import random

class Audio:
    def __init__(self, title, url):
        self.title = title
        self.url = url
        self.ratings = []

    def add_rating(self, rating):
        self.ratings.append(rating)

    def calculate_average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.audio_files = []

    def add_audio(self, audio):
        self.audio_files.append(audio)

    def search_audio_by_name(self, name):
        # Implement audio search logic by name
        pass

    def calculate_playlist_average_rating(self):
        audio_ratings = [audio.calculate_average_rating() for audio in self.audio_files]
        if not audio_ratings:
            return 0
        return sum(audio_ratings) / len(audio_ratings)

class User:
    def __init__(self, name):
        self.name = name

# Generating 3 users and random ratings for demonstration
users = [User(f"User{i}") for i in range(1, 4)]
audio = Audio("Sample Audio", "audio-url")
for user in users:
    random_rating = random.randint(1, 5)
    audio.add_rating(random_rating)

# Displaying the average rating for the audio
print(f"Average Rating for the Audio: {audio.calculate_average_rating()}")

import random
class Audio:
    def __init__(self, name, url):
        self.name = name
        self.url = url
        self.rating = 0

     def add_rating(self, rating):
        self.ratings.append(rating)

    def calculate_average_rating(self):
        if not self.ratings:
            return 0
        return sum(self.ratings) / len(self.ratings)

class Playlist:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.audios = []

    def add_audio(self, audio):
        self.audios.append(audio)

    def calculate_average_rating(self):
        total_ratings = sum(audio.rating for audio in self.audios)
        return total_ratings / len(self.audios) if self.audios else 0


# Example usage:
playlist1 = Playlist("Playlist 1", "Pop")
playlist2 = Playlist("Playlist 2", "Rock")

audios = [Audio(f"Song {i}", f"https://example.com/song{i}.mp3") for i in range(1, 4)]
for audio in audios:
    audio.add_rating(random.randint(1, 5))

playlist1.add_audio(audios[0])
playlist1.add_audio(audios[1])
playlist2.add_audio(audios[2])

average_rating1 = playlist1.calculate_average_rating()
average_rating2 = playlist2.calculate_average_rating()

print(f"Average rating for Playlist 1: {average_rating1}")
print(f"Average rating for Playlist 2: {average_rating2}") '''



