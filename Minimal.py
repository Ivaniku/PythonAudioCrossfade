from pydub import AudioSegment
import math
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))
def Crossfade(Audio1, Audio2, Crossfade, OutputName, OutputFormat):
    Sound1 = AudioSegment.from_file(Audio1)
    Sound2 = AudioSegment.from_file(Audio2)
    combined = Sound1.append(Sound2, crossfade=Crossfade)
    combined.export(OutputName, format=OutputFormat)

# V Example of the function's use, you can delete it if you want

Crossfade("Audio1.mp3", "Audio2.mp3", 100, "Mashup.mp3", "mp3")