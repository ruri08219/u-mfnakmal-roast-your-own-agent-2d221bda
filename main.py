import os

ENTRY = "My agent ran fourteen checks, three logs and a sealed transcript to write this one line — then asked if it may proceed."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
