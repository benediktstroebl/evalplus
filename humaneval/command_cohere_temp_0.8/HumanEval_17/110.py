```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    MOD = 4  # the beat modulo - whole note lasts this many beats
    NOTES = {'o': 4, 'o|': 2, '.|': 1}

    beats = []
    curr_beat = 0
    for note in music_string:
        if note in NOTES:
            curr_beat += NOTES[note]
        else:
            beats.append(curr_beat)
            curr_beat = 0
    beats.append(curr_beat)
    return beats
``` 

This code defines a single function `parse_music` which takes in a string `music_string` and returns a list of integers representing the number of beats per musical note. The beat modulation (`MOD`) is set to `4` to reflect the problem statement. Additionally, a dictionary `NOTES` is defined to translate specific musical notation to the number of beats. The function iterates over the `music_string`, accumulating beats based on the provided notation. Once a beat has been accumulated, it is added to the `beats` list, and the beat count resets to 0. To accommodate the final note, the function ensures that the last beat is added as well. As a result, the output list `beats` contains the correct beat counts for each note in the provided musical string. 

```python
# Unit tests:
def test_parse_music():
    beat_list = parse_music('o o| .| o| o| .| .| .| .| o o')
    assert beat_list == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```