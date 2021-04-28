#Initial code taken from pyaudio's documentation
import pyaudio
import wave
import keyboard
 
#Frames of buffer/amount of time in frames allocated for the program to process the audio.
CHUNK = 1024
#Sets audio format, in this case 16 bit Integer.
FORMAT = pyaudio.paInt16
#Sets number of channels (1 = Mono 2 = Stereo)
CHANNELS = 2
#Sample Rate, the amount of times per second the waveform is sampled.
RATE = 44100
#Sets name of output WAV file.
WAVE_OUTPUT_FILENAME = "output.wav"
 
#Writes data from the list 'frames' to a WAV file. 
def make_wav_file():
    #Creates new wave file with the name 'WAVE_OUTPUT_FILENAME'
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    #Sets amount of audio channels to 'CHANNELS'
    wf.setnchannels(CHANNELS)
    #Sets bit depth using 'FORMAT'
    wf.setsampwidth(p.get_sample_size(FORMAT))
    #Sets amount of samplings per second using 'RATE'
    wf.setframerate(RATE)
    #Conjugates the data obtained from the recording and writes them to the WAV file using 'frames'
    wf.writeframes(b''.join(frames))
    #Closes WAV file
    wf.close()  
 
#Writes the list 'frames' to a txt file for debugging.
def write_frames_to_txt():
    results = open("results.txt", "w")
    results.write("This is The data for the wave file in bytes")
    results.close
    results = open("results.txt", "a")
    results.write(str(frames))
    results.close
 
#Sets up event to check if the s key is being pressed, if it exits the while loop.
is_recording = False
if is_recording == False:
    #Tell user what key start recording
    print("Press s to start recording")
    while is_recording == False:
        if keyboard.is_pressed('s'):
            is_recording = True
 
#Sets up an instance of pyaudio
p = pyaudio.PyAudio()
#Opens audio stream.
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,)
 
 
if is_recording == True:
    #Tells user that the program is recording.
    print("* recording")
    print("Press t to stop recording")
    frames = []
    while is_recording == True:
        #For each second that the stream is open, the list 'frames' will be appended with new data 
        # from the audio stream 'RATE' times per second, in data chunks the size of the 'CHUNK' variable
        # until the user presses the prompted key, in this case 't' to leave the while loop.
        data = stream.read(CHUNK)
        frames.append(data)
        if keyboard.is_pressed('t'):
            is_recording = False
            break
        
        
#Tells user that recording has stopped.
print("* done recording")
 
 
#Ends recording, terminates instance of pyaudio
stream.stop_stream()
stream.close()
p.terminate()
 
#Creates output files
make_wav_file()
write_frames_to_txt()
 
 

