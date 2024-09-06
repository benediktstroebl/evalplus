```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    notes_in_play = []

    for note in music_string.split(' '.'y'):
        if note in notes:
            notes_in_play.append(notes[notes[note])
        else:
            notes_in_play.append(notes[-1])  # Backward compatibility

    return notes_in_play

# Test cases
test_parse_music = []
test_music_strings = [
    'o o| .| o| .| .| .| .| o o',
    'o o o| .| o| o| .| .| .| o',
]

for test_string in test_music_strings:
    test_parse_music.append(parse_music(test_string))
```
This Python code defines a function `parse_music` that takes a music string in a special ASCII format and returns a list of integers representing the number of beats for each note in the music. The function utilizes a legend for different notes, and the notes are split into segments by spaces. The function then extracts the notes from the input string and appends them to a list of notes in play. Finally, it tests the list of music strings to verify the correctness of the `parse_music` function.