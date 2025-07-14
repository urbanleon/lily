import sounddevice as sd
import scipy.io.wavfile as wav
import whisper
import pyttsx3
import os

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def record_audio(filename="input.wav", duration=5, samplerate=44100):
    print("🎙️ Recording for", duration, "seconds...")
    speak("Listening now")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    wav.write(filename, samplerate, recording)
    print("✅ Saved audio as", filename)

def transcribe_audio(filename="input.wav"):
    model = whisper.load_model("base")
    result = model.transcribe(filename)
    print("📝 You said:", result["text"])
    return result["text"].lower().strip()

def handle_command(text):
    if "hello" in text:
        speak("Hi Leo, how can I help you?")
    elif "open calculator" in text:
        os.system("start calc")
    elif "exit" in text:
        speak("Goodbye!")
        exit()
    else:
        speak("I didn't understand that.")

def main():
    speak("LILY is ready.")
    while True:
        record_audio()
        command = transcribe_audio()
        handle_command(command)

if __name__ == "__main__":
    main()
