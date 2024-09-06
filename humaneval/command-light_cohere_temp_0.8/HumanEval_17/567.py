```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    notes_numbers = [notes[note] for note in music_string.return both note and value exist for each letter in music_string.
    return [ list(notes_numbers)

# Test cases
music1 = "o o| .| o| .| .| .| o o"
music2 = "".join"
music3 = "o o o o o"
music4 = "oo"
music5 = "OOO"

test_parse_music = [
    parse_music(music1),
    parse_music(music2),
    parse_music(music3),
    parse_music(music4),
    parse_music(music5)
]
print(test_parse_music)
``` 
This code defines a function **`parse_music`** that parses a music string according to a predefined mapping of notes and beat counts. It then returns a values that correspond to the number of beats each note lasts. The test cases demonstrate the functionality by providing different music strings and expecting the results to be correctly mapped.