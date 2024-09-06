```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ')
   
    each_note in [int(note) for note in music_string.split('\n ', 2)]
    each_note, return [len(note) for note in each_note]

# Test cases
music_cases = [
    "o o| .| o| .| .| .| o o",
    "o o| .| o| .| .| .| o",
    "o o o o| .| o| .| o",
    " ## o o ##",  # Special case: multiple spaces, should still split into single notes
    ]

def test_parse_music(test_cases: List[str]) -> List[List[int]]:
    parsed_notes = []
    for music in test_cases:
        notes = parse_music(music)
        parsed_notes.append(notes)
    return parsed_notes

# Run tests
test_parse_music(music_cases)
``` 
This Python script defines a function `parse_music` that takes a music string in a special ASCII format representing musical notes. The function splits the music into individual notes, and then returns a list of lengths of those notes. The `test_parse_music` function takes a list of test cases, which are strings representing music in the same format. The function then splits each music string into individual notes and returns a list of their lengths. This allows users to easily test the function's functionality.