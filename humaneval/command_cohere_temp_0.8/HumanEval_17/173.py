```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_mapping = {'o': 4, 'o|': 2, '.': 1}
    notes = []
    current_beat = 0
    
    for char in music_string:
        current_beat += beat_mapping.get(char, 0)
        notes.append(current_beat)
    
    return notes
```

This code defines a single function `parse_music` which takes in a string representation of musical notation and returns a list of integers representing the number of beats for each note. The beat mapping serves as a dictionary to map each character to the number of beats it represents. It iterates through the characters of the input string, incrementing the current beat as it encounters each musical symbol, using the `beat_mapping` dictionary, and pads the current beat count with zeroes if it encounters an unknown character. Finally, it returns the list of beat counts. 

To retain the code logic and also improve the code readability, descriptive variables or prefixes were added to the variable names such as `beat_mapping`, `current_beat`, and `notes`. These additions help describe what the subsequent code does or how it is structured. 

This solution avoids the use of any nested or advanced Python features to stay compatible with Python 3.5. Therefore the code should work in most if not all Python versions in common use.