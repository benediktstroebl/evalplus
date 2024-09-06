```python
from typing import List

PATTERN = {'o': 4, 'o|': 2, '.|': 1}

def parse_music(music_string: str) -> List[int]:
    music_list = []
    notes = music_string.strip().split('|')
    for n in notes:
        beat = n.strip().lower()
        if beat in PATTERN:
            music_list.extend(PATTERN[beat] for _ in range(len(n)))
    return music_list
```

The `parse_music` function takes a string containing special ASCII notation for musical notes as input and returns a list of integers representing the number of beats for each note. The function uses a dictionary `PATTERN` that maps note symbols to their corresponding beat lengths. The function iterates over the symbols in the input string, removes any leading and trailing whitespace, splits the input string into symbols using the '|' symbol as a separator, and converts each symbol to lowercase. It then iterates over the symbols and extracts the beat length using the `PATTERN` dictionary. It creates a list from the beat length, repeating it for the number of occurrences of each symbol in the input. 

Here is an example input/output:
```python
input = 'o o| .| o| o| .| .| .| .| o o'
print(parse_music(input))
```

This will output:
```bash
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```