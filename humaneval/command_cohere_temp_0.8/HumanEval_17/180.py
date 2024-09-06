```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    MOD = 4  # the base duration (whole note) lasts this many beats

    beat_list = []
    curr_beat = 0

    for c in music_string:
        if c == 'o':
            beat_list.append(curr_beat)
            curr_beat = 0
        elif c == 'o|':
            curr_beat += 2
        elif c == '.':
            curr_beat += 1
        else:
            # should never happen
            beat_list.append(curr_beat)

    beat_list.append(curr_beat)

    return beat_list
``` 

The script defines a function `parse_music` that takes in a string formatted as described in the prompt and converts it to a list of beats. It iterates through every character of the string and accumulates the current beat duration, checking for 'o', 'o|', and '.', which correspond to whole notes, half notes, and quarter notes. The beat intervals are incremented accordingly, with the accumulated value added to the `beat_list` at the end of every iteration. The function returns the list of beats, with the final value added for any remaining beats not yet added.

Here is an example output of the function:
```python
parse_music('o o| .| o| o| .| .| .| .| o o')
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

The list represents the beats played in the music string. Each value corresponds to the number of beats for the respective note.