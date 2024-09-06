```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_lengths = {'o': 4, 'o|': 2, '.|': 1}
    result = []
    current_beat = 0

    for note in music_string:
        if note in beat_lengths:
            current_beat += beat_lengths[note]
        else:
            result.append(current_beat)
            current_beat = 0

    # Handle the last note
    result.append(current_beat)

    return result
``` 

This script defines a function `parse_music` that takes a string representing musical notes in the given format and returns a list of integers representing the number of beats. It iterates over each note in the string, updating a `current_beat` variable based on the beat length of the note, and storing the value of `current_beat` at the end of each segment defined by a new note.

The `beat_lengths` dictionary is provided in the original challenge description. It maps the special ASCII notation for musical notes provided in the input string to their corresponding beat lengths. This is used to update the `current_beat` variable based on the beat length of each note. 

The function returns the result list, which contains one entry for each segment between notes, representing the number of beats. 

This solution does not require any additional dependencies and can solve the given problem in a self-contained manner. It should be able to pass any tests cases relevant test cases.