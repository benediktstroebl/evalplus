Below is a self-contained Python script that defines a function parse_music that solves the problem you provided earlier.

```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1,
        ' ': 0
    }
    
    beats = 0
    note_lengths = {note: beats for note, beats in notes.
    }
    
    notes = music_string.split(' ')')
   
    notes = [note.split(' |') for note in notes]
    
    notes = [int(note) for note in notes]
    
    return notes

# Test the function
test_music = parse_music('o o| .| o| .| .| .| .| o o')
print(test_music)
```
This script defines a function `parse_music` that takes a string of music notes and returns a list of integers representing the lengths of each note. The function uses a mapping of musical notes to their respective durations. The test case demonstrates the using the function and prints the result.