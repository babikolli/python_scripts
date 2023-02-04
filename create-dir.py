import os

# Create a directory named "new_dir"
os.mkdir("new_dir")

# Change the current working directory to "new_dir"
os.chdir("new_dir")

# Create two empty text files named "file1.txt" and "file2.txt"
open("file1.txt", "w").close()
open("file2.txt", "w").close()
