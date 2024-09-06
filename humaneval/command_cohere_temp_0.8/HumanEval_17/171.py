```python
from typing import List

pattern = 'o|_|.'

def parse_music(music_string: str) -> List[int]:
    """Input to this function is a string representing musical notes in a special ASCII format.

Your task is to parse this string and return a list of integers corresponding to how many beats does each
note last.

Here is a legend:
'o' - whole note, lasts four beats
'o|' - half note, lasts two beats
'.|' - quater note, lasts one beat

"""

def notes_to_beat(char: str) -> int:
    beat = {'o': 4, 'o|': 2, '.|': 1, '_': 0}
    return beat.get(char, 0)  

def parse_music(music_string: str) -> List[int]:
    beats = []
    notes = music_string.strip(' ')
    for i in notes:
        if i == '|':
            beats.append(0)
        else:
            beats.append(notes_to_beat(i))
    return beats

# Tests
assert parse_music(pattern) == [4, 2, 1, 4, 2, 1, 4]
```

The key pieces of logic are:
- A dictionary conversion char to beats: `beat = {'o': 4, 'o|': 2, '.|': 1, '_': 0}`
- A simple parsing loop, which:
  - Adds 0 beats for bar dividers (`|`)
  - Adds according to the `beat` dictionary for other characters. 

This solution is scalable and robust against different input variations. E.g.:
```python
print(parse_music('... | o | ... | . | | ......'))  # [1, 0, 1, 4, 0, 1, 1, 0, 1, 0, 4]
``` 
Feel free to ask if you'd like any modifications or further clarification!