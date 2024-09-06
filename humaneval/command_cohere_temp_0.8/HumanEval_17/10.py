```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    mod = 4  # whole note lasts 4 beats
    beats = []

    current_beat = 0
    for char in music_string:
        if char == 'o':
            current_beat += mod
        elif char == 'o|':
            current_beat += mod // 2
        elif char == '.':
            beats.append(current_beat)
            current_beat = 0
        else:
            raise ValueError("Invalid input format!")

    # finish the last note
    beats.append(current_beat)
    return beats
```

The algorithm works by simply counting the beats as we iterate over the characters of the input string.
We recognize three types of characters:
- 'o' - whole note, increases current beat by 4
- 'o|' - half note, increases current beat by 2
- '.' - beat is a quater note, so we append the current beat to our list and reset it to 0 for the next note. 

To make the algorithm more robust we would need to introduce more tests, especially around edge cases, for example, testing a string where the length of a measure is not a multiple of 4, or testing a string using accidental symbols like '#' or 'b' which are not part of the original specification. 

This solution is relatively simple, performs well and should be easy to understand and maintain for developers with moderate skills. However, we could further optimize it by taking advantage of the fact that the music string probably has a regular structure in terms of beat lengths. So for more performance-critical scenarios, we could use a compressor/decompressor approach that would allow us to process the music in blocks and enforce the correct beat sum for each measure during the parsing process.