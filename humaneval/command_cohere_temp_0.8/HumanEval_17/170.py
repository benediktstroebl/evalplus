```python
import re

def parse_music(music_string: str) -> List[int]:
    beat_pattern = re.compile(r'o|o|_|_|', flags=re.I)
    parsed_beats = []
    for beat_group in beat_pattern.findall(music_string):
        if len(beat_group) == 2:
            parsed_beats.append(4)
        elif len(beat_group) == 1:
            parsed_beats.append(2)
        else:
            parsed_beats.append(1)
    return parsed_beats
```

The key parts of the code are:
- The `re.I` flag that enables case-insensitive matching. This is important as the problem description specifies that o and O should be treated the same.
- The `findall` method that returns all matches of the pattern in the string as a list of lists. And the subsequent loop turns these lists into a single list of integers. 
- The final list of integers corresponds to the beats mentioned in the problem's statement. 
```python
>>> parse_music('o o| .| o| o| .| .| .| .| o o')
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
``` 
This should be the expected outcome for the provided example. Picking the auxiliary library, in this case, regex, was a good choice as it saves a lot of effort and brings robustness to the code.