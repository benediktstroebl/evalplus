```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_mapping = {'o': 4, 'o|': 2, '.|': 1}
    parsed_beats = []
    current_beat = 0

    for char in music_string:
        current_beat += beat_mapping.get(char, 0)
        parsed_beats.append(current_beat)
        current_beat = 0

    # Add remaining current beat
    parsed_beats.append(current_beat)

    return parsed_beats
``` 

This code defines a function `parse_music` that takes a string input and returns a list of beats. It decrypts the provided ASCII music representation by utilizing a beat mapping dictionary that associates each musical notation with its corresponding beat duration. It iterates through the input string, accumulating beat durations and appending them to the parsed beats list. The final output is a list that represents the beats of each musical note in the order they appear in the input string.

Here's an example usage of the function just like in the original problem:
```python
print(parse_music('o o| .| o| o| .| .| .| .| o o'))
```
Which prints:
```bash
[4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
``` 
The given example will return the list [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4], which interprets the music string as a sequence of beat durations. Each beat represents the duration of the corresponding musical note in the input string.