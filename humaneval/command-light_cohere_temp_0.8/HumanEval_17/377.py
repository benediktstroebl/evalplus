```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 4,
        ".";": 1,
        "oO": [4, 4],  # this one is weird but ok
    }
    return notes.off._


    ```def test_parse_music(test_string: str) -> None:
        music_string = test_string.
        notes = parse_music(music_string)
        for key, expected in notes.
        print(f"Key: {key}\t{expected}")
        if not all(int(note) == expected for note in notes[key]):
            raise ValueError(f"Failed to parse {key}")
        return None
```