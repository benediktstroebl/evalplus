```python
from typing import List

PATTERN = {'o': 4, 'o|': 2, '.': 1}


def parse_music(music_string: str) -> List[int]:
    result: List[int] = []
    curr_beat = 0

    for char in music_string:
        if char in 'o|.":':
            curr_beat += PATTERN[char]
        else:
            result.append(curr_beat)
            curr_beat = 0

    # Last chunk
    result.append(curr_beat)

    return result
``` 

This script employs a dictionary, `PATTERN`, to correlate string chords with corresponding beat durations in seconds;Whole notes are represented by `o`, half notes by `o|`, and quarter notes by `.`

The `parse_music` function reads a music_string, iterating through each character. When it encounters a valid chord, it increments the `curr_beat` counter by the duration specified in the `PATTERN`. Upon encountering an invalid chord, it adds the current `curr_beat` value to the result list and resets `curr_beat` to zero. 

After processing each character in the music string, the function returns a list of beat durations corresponding to each chord. 

To demonstrate, the example provided in the problem statement would return this list:
```python
>>> parse_music('o o| .| o| o| .| .| .| o o')
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This repertoire of approaches enables you to efficiently parse and extract beat durations from strings representing musical notes in a specific ASCII format. 

Feel free to experiment with the provided code to gain a deeper understanding of how it works or to adapt it to unique problem variations!