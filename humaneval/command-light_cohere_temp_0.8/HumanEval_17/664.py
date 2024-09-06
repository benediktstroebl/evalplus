Here's a self-contained Python function that parses a music string in a special ASCII format into a list of integers representing the number of beats for each note:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    """
    Input to this function is a string representing musical notes in a special ASCII format.
    The task is to parse this string and return list of integers corresponding to how many beats does each
    last.
    music_string = input("Enter music string: ")
    
    notes = []
    whole = 0
    half = 0
    quarter = 0
    beat = 0

    for note in music_string:
        if note == 'o':
            beat += 1
            whole += 4
        elif note == 'o|':
            beat += 1
            half += 2
        elif note == '|':
            beat += 1
            quarter += 1
        else:
            print("Invalid note. Notes must be 'o o', 'o|', '|', or any other character.")
            return []

    return [beat, quarter, half, whole]
```
This function takes a music string as input and parses it to extract the number of beats for each note. The function handles different cases for the notes and returns an appropriate list of integers.