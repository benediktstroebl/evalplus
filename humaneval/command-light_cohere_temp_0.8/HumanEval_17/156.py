```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beats = music_string.split(' ')
    music_string.split(' '').
    beats.

notes = music_string.split(' ')
beats. for loop i = 0, len(beats) - 1 - i:
    note = beats[i]
    if note in notes:
        yield notes[note] * i // len(beats)
    else:
        raise ValueError("Invalid note!")

# Example usage
music_str = 'o o| .| o| .| .| .| .| o o'
notes = parse_music(music_str)
print(notes)
``` 
This code defines a function `parse_music` that takes a music string as input and returns a list of integers. The integers represent the beats of notes in the music. It uses a legend of notes to map the characters to beat durations.