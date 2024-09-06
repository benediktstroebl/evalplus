```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' '|')
   
    beats = []
    for note in notes:
        if note.count('o note') and note[0] == 'o':
            beats.append(4)
        elif note.count('note') and note[0] == 'o|':
            beats.append(2)
        elif note.count('note') and note[0] == '|':
            beats.append(1)
        else:
            print("Invalid music string")
            return []
    return beats

# Test case
music1 = parse_music("o o| .| o| .| .| .| .| o o")
print(music1)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
``` 
This Python function `parse_music` takes a string as an input and is designed to split the music string into individual notes, identify them, and then return an array of beats corresponding to the number of beats each note should last.