Here is a self-contained Python function that solves the problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split('|')
    formula = ('.join for note in notes if note.split('o.startswith('o duplicates allowed').
    first_half_note = int(note[0]) - 48)
    second_half_note = int(note[1]) - 96
    return [first_half_note, second_half_note]
```
This function takes a string of music written in the format of notes separated by "|", It then splits the string into individual notes, and then uses a formula to calculate the duration of each note in beats. The function then returns a list of durations corresponding to the notes in the music.