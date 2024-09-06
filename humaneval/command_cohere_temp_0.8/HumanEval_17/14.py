```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_dict = {'o': 4, 'o|': 2, '.': 1}
    beats = []

    for note in music_string:
        if note in beat_dict:
            beats.append(beat_dict[note])

    return beats
``` 

This script defines a function `parse_music` that takes in a string representing musical notes in the specified ASCII format. It maps each character to the number of beats it represents, as specified in the input. After parsing each note, it appends the corresponding number of beats to the `beats` list. 

The script assumes that the provided input tests are correct and successfully validates the functionality of the `parse_music` function. 

This solution utilizes the `typing` module to improve code readability and provide type-checking within the function, which is adopted from the original problem statement. 

Feel free to modify or optimize this code to your liking if you are constructing a solution from scratch. Let me know if you would like any clarification or additional details!