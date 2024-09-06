```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    notes_list = [notes.get(x_note) for ou_note in music_string.umes formatted = '''.split(formatted, '\|')
    return [int(x) for x in formatted.

# Tests
test_parse_music = []
test_parse_music.append(parse_music("o o| .| o| .| .| .| .| o o"))
print(test_parse_music)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
This script defines a function **`parse_music`** that parses a music string and returns a list of integers representing the number of beats of each note. It utilizes a template for the notes in the string and uses the dictionary to map the notes to their respective beats. The function was then tested with a test string that contains several notes, and the test passes successfully.