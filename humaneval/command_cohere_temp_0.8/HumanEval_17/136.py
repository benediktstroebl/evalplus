```python
from typing import List

 Pattern = str


def parse_music(music_string: Pattern) -> List[int]:
    beat_lengths = {
        "o": 4,
        "o|": 2,
        ".|": 1,
    }

    result: List[int] = []
    current_beat = 0

    for char in music_string:
        beat_length = beat_lengths.get(char)
        if beat_length: 
            current_beat += beat_length
        else:
            result.append(current_beat)
            current_beat = 0

    # finish the last note
    result.append(current_beat)

    return result
``` 

This code defines a function called `parse_music` that takes a string input, which represents musical notes in a special ASCII format, and returns a list of integers representing the number of beats each note lasts. The beat lengths are defined as follows: `o` - whole note, `o|` - half note, `.|` - quater note. 

The program loops through the special ASCII music string, where each character represents a musical note with a specific beat length. It maintains a `current_beat` variable, which is incremented based on the beat length of each note. When a special character is encountered that doesn't match any beat length, the program adds the current_beat to the result list and resets `current_beat` to 0, preparing to count the beats for the next note. Finally, after processing the entire string, the program adds the final value of `current_beat` to the result list, accounting for the beat length of the last note. 

This code would be easy to integrate within a larger Python project and can be tested individually using `pytest`. 
For more complex tests, the `unittest` framework can be used as part of the Python standard library.