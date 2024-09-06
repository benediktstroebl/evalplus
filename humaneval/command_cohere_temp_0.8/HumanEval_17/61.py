```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_mapping = {'o': 4, 'o|': 2, '.|': 1}
    beats = []

    current_beat = 0
    for char in music_string:
        if char in beat_mapping:
            current_beat += beat_mapping[char]
            beats.append(current_beat)
            current_beat = 0
    # Add remaining current beat
    beats.append(current_beat)

    return beats
``` 
The script defines a function `parse_music` that takes a string input and returns a list of integers representing the number of beats for each note. The beat mapping is initialized with the mapping of each character to its corresponding number of beats. It iterates through the characters of the music string, and when it encounters a character present in the `beat_mapping`, it increments the `current_beat` accordingly and appends it to the `beats` list. Finally, it returns the list of beats. 

This solution adheres to the given test case and provides a functionality to parse the music string and return the number of beats for each note.