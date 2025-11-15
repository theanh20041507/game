
from PIL import Image
import os

# Tạo thư mục assets nếu chưa có
os.makedirs("assets", exist_ok=True)

# Tạo ảnh tủ lạnh trống
fridge = Image.new("RGBA", (300, 500), (0, 0, 0, 0))  # trong suốt
fridge.save("assets/fridge.png")

# Tạo 5 ảnh học sinh trống
for i in range(1,6):
    student = Image.new("RGBA", (60, 60), (0,0,0,0))  # trong suốt
    student.save(f"assets/student{i}.png")

# Tạo 5 file âm thanh trống (1 giây) dạng WAV
import wave

def create_silence(filename, duration_sec=1):
    framerate = 44100
    nframes = duration_sec * framerate
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(framerate)
        wf.writeframes(b'\x00\x00' * nframes)

create_silence("assets/tick.wav")
create_silence("assets/success.wav")
create_silence("assets/fail.wav")
create_silence("assets/openDoor.wav")
create_silence("assets/bgm.wav")

print("Đã tạo xong thư mục assets với ảnh và âm thanh trống.")
