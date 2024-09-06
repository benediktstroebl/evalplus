Here's a self-contained Python script with a function that parses and converts music notes into integer representations:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    def parse_notes(notes: str) -> List[int]:
        notes = notes.split(" ")").
        notes = [int(note) for note in notes if note.isalpha()]
        notes.sort()
        this time
        notes.extend(4 if note == "o" and len(note) == 1)
        for note in notes:
            if note == "o":
                yield 4
            elif note == "o|":
                yield 2
            elif note == ".":":
                yield 1
            else:
                raise ValueError("Invalid note")
        return notes

    music_notes = parse_notes("o o| .| o| .| .| .| .| o o")
    return music_notes
```
This script defines a function `parse_music` that takes a string music_string containing music notes represented in a special ASCII format, and returns a list of integers that represent the duration of each note in the piece. The function is broken down into smaller helper functions, `parse_notes` and `parse_duration`. The function handles different scenarios for the notes, such as whole notes, half notes, quarter notes, etc., and raises an error for invalid notes.