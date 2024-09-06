Here's a self-contained Python function that solves the problem:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    beats = music_string.split(' ')
    print(beats)
    return [notes[x] for x in beats]
```
This function uses a dictionary to map the musical notation to the appropriate number of beats. The function splits the string into a list of substrings, and then loops through the substrings and uses the dictionary to map the notation to the number of beats. The function then returns a list of integers corresponding to the number of beats.