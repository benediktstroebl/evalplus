```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '.|': 1
    }
    return [notes[note] for note in music_string.test_music('oo o| .| o| .| .| .| .| o o')]
```
This code defines a function **`parse_music`** that parses a music string. It uses a to match the notes with their respective beats using a dictionary. The main idea is to loop through each character in the string and to check if it's a valid musical note, returning the beat for that note. The final list of integers that represent the total beats for each note is returned.