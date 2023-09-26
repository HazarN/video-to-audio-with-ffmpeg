import os
import subprocess as sb

def create_directory(dir_name):
    if not os.path.exists(f'../{dir_name}'):
        os.mkdir(f'../{dir_name}')

def convert_to_mp3(input_file, output_file):
    create_directory('outputs')

    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_file,
        "-vn",
        "-acodec", "libmp3lame",
        "-ab", "192k",
        "-ar", "44100",
        "-y",
        output_file
    ]

    try:
        sb.run(ffmpeg_cmd, check=True)
        print('Conversion complete!')
    except sb.CalledProcessError as e:
        print('Conversion failed!\nCode: ', e.returncode)

for i, file_name in enumerate(os.listdir('../assets')):
    print(file_name)
    convert_to_mp3(f'../assets/{file_name}', f'../outputs/{i}.mp3')

print(
"""
********************************************
    All files converted successfully!
********************************************
""")