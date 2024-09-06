```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    beat_mapping = {'o': 4, 'o|': 2, '.': 1}
    parsed_music = []
    current_beat = 0

    for char in music_string:
        current_beat += beat_mapping.get(char, 0)
        parsed_music.append(current_beat)

    return parsed_music
```

This code defines a function `parse_music` that takes a string representation of musical notation and returns a list of beats. The beat mapping dictionary translates each notation character into its corresponding beat value. The code iterates through the input string, accumulating beat values using the `beat_mapping` dictionary and storing the resulting beats in the `parsed_music` list. 

To ensure proper functionality, let's test this code using the example provided, as well as a test that covers all the note types:
```python
def test_parse_music():
    beat_mapping = {'o': 4, 'o|': 2, '.': 1}
    assert parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    assert parse_music('o| o|. o| .| .| o| .| .| o') == [2, 4, 1, 1, 2, 1, 1, 1, 0, 4]
```