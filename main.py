import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100
second = int(input("Enter time duration: "))
record_voice = sd.rec(int(second * fs), samplerate=fs,channels=2)
sd.wait()
sd.default.device = 'Microsoft Sound Mapper - Input'
write('Microsoft Sound Mapper - Input', fs, record_voice)
print("Finished.....\nPlease check your output file.")
