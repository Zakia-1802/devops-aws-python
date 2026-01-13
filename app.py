#!/usr/bin/env python3
from datetime import datetime
import os

# créer le dossier logs s'il n'existe pas
os.makedirs("logs", exist_ok=True)

msg1 = "Hello AWS DevOps"
msg2 = "Logging enabled"

with open("logs/app.log", "a") as f:
    f.write(f"{datetime.now().isoformat()} INFO {msg1}\n")
    f.write(f"{datetime.now().isoformat()} INFO {msg2}\n")

print(msg1)
print(msg2)

