Here is a Python script that defines a function that parses a music string and produces a list of note lengths.
```python
def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 4,
        ".":|": 1,
        "...": 4,
    }
    return [notes[char] for char in music_string.
```
This function parses a music_string into a list of note lengths, which is done by checking each character in the string against the characters in the notes dictionary.