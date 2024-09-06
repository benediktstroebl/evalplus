Here is a Python script that demonstrates a self-contained function to parse and transform markdown code into a list of integers:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 1,
        ".":.":": 1,
        ".":o": 4,
        "o|": 2,
        "|.":": 1,
    }

    result = []
    for note in music_string.split(" "|"):
        if note in notes:
            result.append(notes)
    notes[note]

def test_parse_music():
    music_str = "o o| .| o| .| .| .| .| o o"
    result = parse_music(music_str)
    print(result)
    print(len(result))

test_parse_music()
```

This script defines a function `parse_music` that takes a string music_string as input and returns a list of integers. The function utilizes a `notes` dictionary to map the musical notes to their corresponding durations. The function then iterates through the notes in the string and appends the durations to the result list. The `test_parse_music` function is then used to test the `parse_music` function with a sample input. 

This code demonstrates the principle of self-containment, as the function can be understood and used without relying on any external code or dependencies.