from pydub import AudioSegment
import os

def mp3_to_wav(input_path, output_path):
    try:
        # Load the MP3 file using pydub
        audio = AudioSegment.from_mp3(input_path)

        # Export the audio as WAV
        audio.export(output_path, format="wav")

        print(f"Successfully converted {input_path} to {output_path}")
    except Exception as e:
        print(f"Error converting {input_path} to {output_path}: {e}")

if __name__ == "__main__":
    try:
        # Get the current working directory
        current_directory = os.getcwd()

        # Ask the user for the MP3 file name
        input_filename = input("Enter the name of the MP3 file (including the extension): ").strip()

        # Construct the full input file path
        input_path = os.path.join(current_directory, input_filename)

        # Check if the file exists
        if not os.path.isfile(input_path):
            print("File not found:", input_path)
        else:
            # Check if the file is an MP3
            _, file_extension = os.path.splitext(input_filename)
            if file_extension.lower() != ".mp3":
                print("Please provide an MP3 file.")
            else:
                # Get the output file path by changing the extension to .wav
                output_filename = os.path.splitext(input_filename)[0] + ".wav"
                output_path = os.path.join(current_directory, output_filename)

                # Convert the MP3 to WAV
                mp3_to_wav(input_path, output_path)
    except KeyboardInterrupt:
        print("\nConversion aborted by the user.")
