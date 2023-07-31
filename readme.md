# Step 1: Clone the Repository
If you are downloading from the release, you can skip this.
Open your terminal or command prompt.
Change to the directory where you want to clone the repository.
```command
git clone https://github.com/axeltechtips/MP3ToWAV.git
```
# Step 2: Install Required Dependencies
Navigate to the cloned repository's directory:
cd MP3ToWAV
Install the required dependencies using pip:
```python
pip install pydub
```
Step 3: Run the MP3 to WAV Conversion Script
Place the loversrock.mp3 (or any other MP3 file you want to convert) in the same directory as the script (mp3_to_wav_converter.py).

Run the script using the following command:

```python
python convert.py
```
The script will prompt you to enter the name of the MP3 file (including the extension) you want to convert. For example, if your MP3 file is named loversrock.mp3, type loversrock.mp3 and press Enter.
To make it easier, add the MP3 file to where your folder with the scripts are.

The script will convert the MP3 file to a WAV file with the same name and place it in the same directory.

# Step 4: Check the Converted WAV File
You should now have a new file named loversrock.wav (or the name of your MP3 file with the .wav extension) in the same directory.

You can use any media player that supports WAV files to play the converted file.

# Step 5: Add Metadata (Optional)
If you want to add metadata to the WAV file, you will have to use a ID3 Tag Editor like https://www.mp3tag.de/en/.

# Information
You need to have ffmpeg and ffprobe in your path, or in the folder with the command. Go to https://ffmpeg.org/download.html and get ffmpeg and ffprobe.
