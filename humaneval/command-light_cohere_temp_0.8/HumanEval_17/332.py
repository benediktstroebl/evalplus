```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    beat = []
    for note in music_string.split(' '.' provided by the only the note and its duration will be in the format <note> <beat>, i.e.e, < whole note. All others aHow is an line for each note, with a newline. Then, we will have a list of beat, where each beat is the total duration of all notes in the line.

test_music = """
    o o| .| o| .| .| .| .| .| o o
"""

test_parse = parse_music(test_music)

print(test_parse)
```