```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_mapping = {'o': 4, 'o|': 2, '.': 1}
    parsed_beats = []
    notes = music_string.split('|')
    
    for i, note in enumerate(notes):
        beat = sum(beat_mapping[char] for char in note if char in beat_mapping)
        parsed_beats.extend([beat] * (i + 1))
    
    return parsed_beats
``` 

This script defines a `beat_mapping` dictionary to map each ASCII character to the number of beats it represents. It then iterates over each note string in the `music_string`, summing the beats of each character in the note using a list comprehension and assigning the total beats to a variable. It repeats this process for each note, incrementing the beat count by 1 for each new note. Finally, it returns the list of beat counts. 

This approach allows the code to handle multiple notes of different lengths in a single string and provides a clear structure for managing the state of beat counts for each note. 

Such code structure promotes code readability, and maintainability, helping other developers understand the functionality of code with ease.