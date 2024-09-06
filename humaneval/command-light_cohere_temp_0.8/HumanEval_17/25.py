```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(" ")
    whole_notes = []
    for note in music_string:
        note_pair = note.split("|")
        notes.length = int(note_pair[0])
        beat = int(note_pair[1])
        if length == 4 and beat == 2:
            whole_notes.append(beat)
        elif length == 2 and beat == 1:
            whole_notes.append(beat)
        else:
            quarter_notes.append(beat)
    return quarter_notes

# Test cases
test_string = "o o| .| o| .| .| .| o o"
test_notes = parse_music(test_string)
print("Test string:", test_string)
print("Test notes:", test_notes)
```
This script defines a function, `parse_music`, which takes a string as input and parses it into a list of integers. The function separates the string into individual notes, and then separates each note into its length (number of beats) and beat (whether it's a whole or quarter note). The function then uses these values to create the corresponding list of notes, and returns it.