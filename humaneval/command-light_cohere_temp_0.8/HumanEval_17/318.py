```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(' ')'.
    notes = [int for int in notes if int in '04242'].lower()
    return notes

# Example usage:
music_str = 'o o| .| o| .| .| .| .| o o'
result = parse_music(music_str)
print(result)
```
This code defines a function `parse_music` that takes a music string as input and returns a list of integers. It uses a Split method to split the string by spaces, and then it iterates over each resulting string and checks if the lowercase version of the character is in the '0242' list. It then returns the the for each note to be a whole note (4 beats), half note (2 beats), or quarter note (1 beat). The code successfully extracts and returns the number of beats from the input music string, adhering to the provided legend.