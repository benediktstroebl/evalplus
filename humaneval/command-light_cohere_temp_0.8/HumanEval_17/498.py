Here is a self-contained Python script that defines a function `parse_music` which takes a string of music notes and parses it to a list of integers, representing the duration of each note in beats:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 4,
        ".":|": 1,
        ".": 4,
        ".":": 1,
    }
    
    beats = music_string.split('|')
    beats
    notes. Then, we loop through each '.'beats and get the note from the notes dictionary. Finally, we append the beats with the notes.

# Test case 1
music_string = 'o o| .| o| .| .| .| o o'
# Test case 2
music_string = 'o o| o| .| .| o .| o| .| .| .| .| .| o'
```