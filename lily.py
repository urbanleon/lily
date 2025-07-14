import sounddevice as sd
import scipy.io.wavfile as wav
import whisper
import os

COMMANDS = {
    "open calculator": lambda: os.system("calc" if os.name == "nt" else "gnome-calculator"),
    "hello": lambda: print("Hi Leo, how can I help you?"),
    "exit": lambda: exit(0),
}

def record_audio(filename="input.wav", duration=5, samplerate=44100):
    print("🎙️ Recording for", duration, "seconds...")
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
    for command, action in COMMANDS.items():
        if command in text:
            print(f"⚙️ Executing command: {command}")
            action()
            return
    print("❓ Command not recognized.")

def main():
    print("🧠 LILY is listening. Speak clearly after the beep.")
    while True:
        record_audio()
        spoken_text = transcribe_audio()
        handle_command(spoken_text)

if __name__ == "__main__":
    main()
