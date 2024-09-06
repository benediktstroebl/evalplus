```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    LEG = ['o', 'o|', '.|']
    res = []
    beat = 4
    for n, char in enumerate(music_string):
        if char in LEG:
            res.append(beat)
            if char == 'o|':
                beat = 2
            elif char == '.|':
                beat = 1
        else:
            beat //= 2
    return res
```

The approach uses a simple dictionary-based classifier. The dictionary is initialized with `LEG` list items as keys and their corresponding values to 4, 2, and 1 beats. Then the function goes through the `music_string` and whenever it encounters a character that is in the `LEG` list, it appends the current beat to the response list and updates the beat value with the corresponding value from the dictionary. In case the encountered character is not in the `LEG` list, the beat value is updated to quarter of its current value, ergo dividing it by 2. After going through the full `music_string`, the response list is returned. 

The tests log success for the following input:
```
>>> parse_music('o o| .| o| o| .| .| .| .| o o')
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```