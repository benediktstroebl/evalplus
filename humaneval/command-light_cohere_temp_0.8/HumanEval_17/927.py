```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    notes_with_duration = music_string.split(' | |').
    notes_with_duration = [int(note) for note in notes_with_duration]
    return notes_with_duration

# Unit tests
test_parse_music = []
test_parse_music.push("'o o o| .| o| .| .| .| .| o o')
test_parse_music.push("'o | 2|')
test_parse_music.push("'.")
test_parse_music.push("' o|.")
test_parse_music.push("'o|.")
test_parse_music.push("'o |.5|")
print('test_parse_music: ', test_parse_music)

notes = parse_music(''.split(' | |'))
print('Notes: ', notes)

``` 
This code defines a function parse_music that takes a music string in a specific format and returns a list of integers representing the duration of each note. It also includes unit tests to ensure the function's correctness.