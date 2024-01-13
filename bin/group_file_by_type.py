import os
import shutil
import sys

if sys.argv[1] != None:
    path = sys.argv[1]
else:
    path = "."

# Get list of files
files = [f for f in os.listdir(path) if os.path.isfile(path + "\\" + f)]


# Get list of extensions and remove duplicated
extensions = set([f.split(".")[-1].lower() for f in files])


# Create folder for each extension
try:
    for ext in extensions:
        os.makedirs(path + "\\" + ext)
except Exception:
    print("Moving to existing folder with same name", Exception)

# Move files to their folder with extension name
for f in files:
    try:
        shutil.move(path + "\\" + f, path + "\\" + f.split(".")[-1].lower() + "\\" + f)
    except Exception:
        print("Unable to move file", path + "\\" + f)
