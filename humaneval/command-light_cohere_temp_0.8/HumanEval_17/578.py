Below is a Python script with a self-contained function that parses a music notation string into a list of integers representing the number of beats for each note.

```python
import typing

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '|': 1,
        '.': 1
    }
    return [notes[note] for note in music_string.test_music_string]
```

This function uses a dictionary `notes` to map music notation characters to the number of beats each one lasts. It then iterates over each character in the input string, and returns a list of the corresponding number of beats.