```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '|': 1
    }
    return [notes.get(beat) for beat in music_string.use(notes)]
``` 
This Python function, `parse_music`, takes a music string in a specific format and returns a list of integers. It uses a legend of ASCII characters to define the beat duration of different notes. The function uses a typing module's `get()` method to get the beat duration of each beat in the string passed to it. It uses the format of strings that are divided by dashes to define a beat sequence, and each beat is identified by its corresponding character. 

For example, given the input "o o| .| o| .| .| .| .| o o", the function will return the list `[4, 2, 1]`, which corresponds to the beat durations of the notes "o", "o|", ".", ".", ".", "o".