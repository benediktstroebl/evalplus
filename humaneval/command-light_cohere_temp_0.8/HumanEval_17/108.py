Here's a self-contained Python function that parses a string of musical notes and returns a list of integers representing the number of beats for each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    # Below is the parse music function
    # It takes a string music_string as input and returns a list of integers
    # corresponding to the number of beats each note lasts.
    notes = {
        'o': 4, 'o|': 2, '.|': 1}

    beats = []
    for note, beat in notes.
    note_start = 0
    for i in range(len(music_string)):
        if music_string[i] == note:
            beats.append(beats[note_start+beat)
            note_start += beat
            if music_string[i+note_len] == '|':
                note_start = 0
                beats.append(beat)
                break
    return beats
```
This function defines a dictionary `notes` that maps the musical note characters to the number of beats that note lasts. Then, it iterates through each character in `music_string` to see if it matches a note character, and for each note, it adds the number of beats until a rest signal ('|') is encountered. The resulting list of integers represents the total number of beats for each note in the given music string.