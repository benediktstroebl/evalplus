```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '|', '.']
    beats = [4, 2, 1, 2, 1, 1, 4]

    beats = [int(beat) for beat in beats]

    notes = [int(note) for note in notes]

    return notes

# Test cases
test_cases = [
    'o o| .| o| .| .| .| .| o o',
    [4, 2, 1, 2, 1, 1, 1, 1, 4, 4],
    'o o| .|.o.',
    [4, 2, 1],
    '.|', [1],
    'o o o', [4, 4],
    ' WHOLEL', [4]
]

def test_parse_music():
    for music_str, expected_beats, expected_notes in test_cases:
        actual_beats = parse_music(music_str)
        assert len(actual_beats) == expected_beats
        assert all(beat == expected_beats[i] for i, beat in enumerate(actual_beats))
        actual_notes = parse_music(' '.join.')[1:]
        assert len(actual_notes) == expected_notes
        assert all(note == expected_notes[i] for i, note in enumerate(actual_notes))

test_parse_music()
``` 
This code defines a function `parse_music` that takes a music string and returns a list of its beats. The function uses predefined music notation to convert the string into the desired format. 

This code is a good example of a self-contained function that can be used for further applications.