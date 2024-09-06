```python
from typing import List

 Patterns = {
    'o': 4,
    'o|': 2,
    '.|': 1,
}


def parse_music(music_string: str) -> List[int]:
    result = []
    notes = []

    current_note = None
    beat = 0

    for char in music_string:
        if char in 'o|.' and current_note is None:
            current_note = char
        elif char in 'o|.' and current_note is not None:
            notes.append(beat)
            beat = beat + Patterns[current_note]
            current_note = None
        elif char == '|':
            if current_note is not None:
                notes.append(beat)
                beat = 0
                current_note = None
        elif char == '.':
            if current_note is None:
                raise ValueError("Invalid note format!")
        else:
            raise ValueError("Invalid note format!")

    if current_note is not None:
        notes.append(beat)

    return notes
```

The algorithm works by simply iterating over each character in the string. We keep track of the current note and its beat length. When we encounter a bar ('|'), we add the current beat to the list of notes and reset the beat counter. If we encounter a new note, we update the current note and beat length accordingly. 

To ensure that the algorithm terminates, we add a check to validate the input format. If we encounter a dot ('.') without a prior note, it will throw a ValueError, as this scenario indicates an invalid input.  This way, the algorithm will output the correct number of beats per note in the given music string.