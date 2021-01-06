from pydub import AudioSegment
from pydub.playback import play
import subprocess
from playsound import playsound
import math
import re
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))
def GetLenght(Input):
    result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', os.getcwd() + os.path.sep + Input], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return float(result.stdout)

def FindFile(File):
    if os.path.isfile(File):
        print ("Found the file " + File)
        print ("Duration of the file: " + str(math.floor(GetLenght(File) * 1000)) + "ms \n")
        return(File)
    else:
        print (f"I can't find the file {File}, please specify me the name of the first audio. It must be in " + os.getcwd())
        try:
            File = input()
        except:
            print ("I couldn't find that file, remember it must be in this type of format: MyAudio.myaudioextension")
            exit()
        else:
            if os.path.isfile(File):
                print ("Found the file " + File)
                print ("Duration of the file: " + str(math.floor(GetLenght(File) * 1000)) + "ms \n")
                return(File)

try:
    File1 = FindFile("Audio1.mp3")
    File2 = FindFile("Audio2.mp3")
    Sound1 = AudioSegment.from_file(File1)
    Sound2 = AudioSegment.from_file(File2)
    try:
        Crossfade = int(input("Enter the crossfade in miliseconds: "))
        if math.floor(GetLenght(File1) * 1000) < Crossfade:
            print(f"The crossfade is longer than {File1}! Changing the crossfade to a proper value...")
            Crossfade = int(math.floor(GetLenght(File1) * 1000) / 2)
        if math.floor(GetLenght(File2) * 1000) < Crossfade:
            print(f"The crossfade is longer than {File2}! Changing the crossfade to a proper value...")
            Crossfade = int(math.floor(GetLenght(File2) * 1000) / 2)
    except ValueError:
        Crossfade = int(math.floor(GetLenght(File1) * 1000) / 2)
        print(f"No valid value has been given, defaulting to {Crossfade}ms.")
    print(f"Crossfading {File1} and {File2} with a {Crossfade}ms crossfade")
    print(Crossfade)
    combined = Sound1.append(Sound2, crossfade=Crossfade)
    combined.export("Mashup.mp3", format="mp3")
    print(f"2 audios crossfaded successfully")
    playsound("Mashup.mp3")
except:
    print("Something failed")
    exit()