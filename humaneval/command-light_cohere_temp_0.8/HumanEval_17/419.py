```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4, "o|": 2, ".":": 1,
        ".":": 1,
        "..": 4,
        "oO": 8,
        "oO|": 4,
        "oo|": 2,
        "O|": 1,
        "O":"",
    }
    
    pattern = r"[{]<}", "O": "o", "oO": "oO", "oo": "oo",
        "o|": "o", "O|": "O",
        "oo|": "oo",
        "|":"|",
        ".";: "."
    }
    
    pattern_reverse = r"[ .{<}]}"

    notes_list = music_string.findall(pattern, reverse=True)
    notes_dict = {note: notes[note] for note in notes_list}
    
    return notes_dict.from(note: notes[note] for note in notes_dict)
``` 
This code defines a function `parse_music` that takes a string representing a piece of music and parses it into a list of integers, where each integer represents the number of beats for each note. 

The parsing is done using a dictionary of note names and their corresponding durations, and a regular expression pattern to find these notes in the music string.