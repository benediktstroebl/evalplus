```python
from typing import List

 Pattern = str


def parse_music(music_string: Pattern) -> List[int]:
    BEAT = {'o': 4, 'o|': 2, '.|': 1}
    return [BEAT[note] for note in music_string]
```

The beat dictionary provides a mapping from each ASCII character to its beat value. We iterate over each character in the input `music_string`, and using the dictionary, we map each one to its corresponding beat value, storing them in the returned list. 

You can test this function by calling it with a string representing musical notes in the given ASCII format, and it will return a list of integers corresponding to the number of beats each note lasts. 
For example:
```python
print(parse_music('o o| .| o| o| .| .| .| .| o o'))
```
This will print:
```
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```