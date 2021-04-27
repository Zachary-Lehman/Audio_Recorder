#Intitial code taken from pyaudio's website
import pyaudio
import wave
import keyboard

#Frames of buffer/amount of time in frames allocated for program to process the audio.
CHUNK = 2048
#Sets audio foramat, in this case 16 bit Integer.
FORMAT = pyaudio.paInt16
#Sets number of channels (1 = Mono 2 = Stereo)
CHANNELS = 2
#Sample Rate, the amount of times per second the waveform is sampled.
RATE = 44100
#Sets name of output WAV file.
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

def make_wav_file():
    #Creates new wave file with the name 'WAVE_OUTPUT_FILENAME'
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    #Sets amount of audio channels to 'CHANNELS'
    wf.setnchannels(CHANNELS)
    #Sets bit depth using 'FORMAT'
    wf.setsampwidth(p.get_sample_size(FORMAT))
    #Sets amount of samplings per second using 'RATE'
    wf.setframerate(RATE)
    #Conjucates the data obtained from the recording and writes them to the WAV file using 'frames'
    wf.writeframes(b''.join(frames))
    #Closes WAV file
    wf.close()  

def write_frames_to_txt():
    results = open("results.txt", "w")
    results.write("This is The data for the wave file in bytes")
    results.close
    results = open("results.txt", "a")
    results.write(str(frames))
    results.close

is_recording = False
if is_recording == False:
    print("Press s to start recording")
    while is_recording == False:
        if keyboard.is_pressed('s'):
            is_recording = True

#Sets variable stream equal to the output of the function open with the previously established parameters as variables.
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,)

if is_recording == True:
    #Tells user that the program is recording.
    print("* recording")

    frames = []

    print("Press t to stop recording")
    while is_recording == True:
        #For each sampling from zero to sample rate over buffer times the amount of recording time, adds the data at that point to the list 'frames'.
        data = stream.read(CHUNK)
        frames.append(data)
        if keyboard.is_pressed('t'):
            is_recording = False
            break
        
        
#Tells user that recording has stppoed.
print("* done recording")


#Ends recording, terminates instance of pyaudio
stream.stop_stream()
stream.close()
p.terminate()

make_wav_file()
write_frames_to_txt()

