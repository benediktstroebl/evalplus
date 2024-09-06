```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Your function takes a string as input and returns a list of integers.
    music_string = input("Please input the music format: ")
    notes = []

    #split the music string by "|"
    music_split = music_string.split("|")
   
    # loop over the music split and appends the beat counter
    for note in music_split:
        if note[0] == ".":
            notes.append(1)
        elif note == "o":
            notes.append(4)
        elif note == "o/":
            notes.append(2)
        elif note == ".":
            notes.append(0)
        else:
            notes.append(1)

    # return the list of beat counter
    return notes

#test case
music_string = input("Please input the music string: ")
print(parse_music(music_string))
```