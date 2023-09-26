# mp4-to-mp3
This app is a conversion program of video files to audio files. Program is written in python.

# Manual:
To use it, open a directory called "assets". Then move your video files (.mp4, .mpeg, .mov etc.). Then open a terminal and go to the src\main.py directory and run the program.
Example: > cd move/the/directory/.../src ; python3 main.py

# Intuition
Code is actually very simple. It uses simple os and subprocess manipulations in python libraries. The main part is called "ffmpeg". You need to download ffmpeg and install it first. Code is just uses some ffmpeg parameters in a list and runs them in order.
