Here is a self-contained Python function that takes a string of music notes in a special ASCII format and returns a list of integers representing how many beats each note lasts:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|' : 2,
        '.|' : 1
    }
    return [notes[note] for note in music_string.get()]
```
This function uses a dictionary to map musical note characters to the number of beats the note lasts. 

Here's a brief explanation of how the function works:
1. The function `parse_music` takes a string music_string as input.
2. Using a `notes_dict` and `get` method, it creates a dictionary that maps musical note characters to the number of beats that note lasts.
3. The `get` method is used to iterate over each character in the music_string and map it to its corresponding number.
4 The resulting list of integers is returned.