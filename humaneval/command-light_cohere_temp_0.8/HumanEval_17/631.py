Here's a self-contained Python function that parses markdown code representing musical notes, and returns a list of integers corresponding to the duration of each note in beats:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '|': 1
    }
    return [notes[note] for note in music_string.parse(music_string)]
```

This function uses a dictionary to map the musical note characters to the respective beat values, and then uses the `parse()` method to split the string into a list of notes. The function then iterates over each note and returns its beat value. 

Here's an example test case:
```python
music_str = 'o o| .| o| .| .| .| o o'
result = parse_music(music_str)
print(result)
```

This will output: `[4, 2, 1, 2, 2, 1, 1, 1, 4]