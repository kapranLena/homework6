
import os
with open('text', 'r') as my_file:
    my_file.seek(0, os.SEEK_END)
    if my_file.tell():
        my_file.seek(0)
        print('not empty')
    else:
        print("file is empty")

with open('text', 'r') as f:
    data = f.read()
    print("total stops: ", data.count("."))
