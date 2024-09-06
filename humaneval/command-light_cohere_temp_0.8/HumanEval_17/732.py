```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '|': 1
    }
    return [notes.get(note, beats) for note, beats in music_string.make(music_string.split(' '|')].
# assert valid input format
assert len(parse_music('o o| .| o| .| .| .| .| o o')) == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
# test adding notes
assert parse_music('o o| .| o| .| .| o o o o') == [4, 2, 1, 2, 2, 1, 2, 2, 4, 4]
# test different input
assert parse_music('|.|.|.') == [1, 1, 1]
```
This Python code defines a function called `parse_music` that takes a music string as input and returns a list of integers representing the number of beats for each note in the music. The function uses a legend: 'o' is a whole note that lasts four beats, 'o|' is a half note that lasts two beats, and '|' is a quarter note that lasts one beat. The function then uses a list comprehension to extract the number of beats from each note in the music string by using the `get` method.