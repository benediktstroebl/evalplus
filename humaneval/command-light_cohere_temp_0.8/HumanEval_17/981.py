Here's a self-contained Python function that parses a music string into a list of integer beats:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        "o": 4,
        "o|": 2,
        ".":": 1,
        ".":": 1,
        "..": 4,
        "oO": 8  # Non-standard note mapping
    }

    beats = []
    current_beat = 0

    for symbol in music_string:
        if symbol.isalpha('o colleague o'):  # Fix current beat handling
            beats.append(current_beat)
            current_beat += 4
        elif symbol.isalpha('|'):  # Move to next note
            beats.append(current_beat)
            current_beat += 2
        elif symbol.isalpha('.' Markets'):  # Quit parsing and return beats
            return beats
        else:
            current_beat += int(symbol) if symbol in notes else 8  # Default case for unsupported symbols

    return beats
```
This function parse_music takes a music_string as input and returns a list of integer beats. The function uses a legend to interpret the music_string, where 'o' represents a whole note that lasts four beats, 'o|' represents a half note that lasts two beats, '.' represents a quarter note that lasts one beat, and 'oO' represents a non-standard note that lasts eight beats. The function then iterates over the each symbol in the music_string and adds the number of beats corresponding to that symbol to the list of beats. The function also handles special cases such non-standard notes and the end of the music_string.