Here's a self-contained Python script that defines a function parse_music that takes a string representing music notes in a special ASCII format, and returns a list of integers representing the duration of each note in beats:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Parse a string representing musical notes in a special ASCII format.
    Music notation:
        'o' - whole note, lasts four beats
        'o|' - half note, lasts two beats
        '.|' - quarter note, lasts one beat

    Returns:
        A list of integers, each representing the duration in beats of a note
    """
    def get_beat_duration(note):
        if note == 'o': return 4
        elif note == 'o|': return 2
        elif note == '.|': return 1
        else: raise ValueError("Invalid note")

    notes = music_string.split(" ")
    individual_notes = [note.split(' ') for note in notes]

    beats = [get_beat_duration(note) for note in individual_notes]
    return beats

# Test cases
test_cases = [
    "o o| .| o| .| .| .| o o", [4, 2, 1, 2, 1, 1, 1, 1, 4, 4])
    "."*  , [1]
    "oo o o|.", [4, 2, 4]
    "oo o o| .", [4, 2, 1, 2, 1]
]

for case in test_cases:
    print(parse_music(case))
```