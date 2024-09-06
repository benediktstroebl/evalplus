Here is a self-contained Python script that defines a function `parse_music` solving the problem of parsing musical notes represented as ASCII:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    beat_counts = {note: value for note, value in notes. beats notes} static
    static_loop_detection = {}
    for char in music_string:
        if char in notes:
            static_loop_detection[char] = (static_loop_detection.get(char, 0) + 1) % notes[char]
        else:
            raise ValueError("Invalid note character")
    
    return [beat for beat in range(1, max(static_loop_detection.get(char), static_loop_detection[char]) + 1)]
```
This function utilizes a dictionary to map musical notes to their corresponding beat counts, and then iterates through each character in the input string. The loop detection process counts the beats for each note and determines the beat count for each loop. 

Finally, the function returns the list of beat counts corresponding to the input music string.