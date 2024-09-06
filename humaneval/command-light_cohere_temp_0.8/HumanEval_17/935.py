```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    notes. pinning_list = ['.join(notes.get(x, music_string, 4))
    return notes_list

def test_music():
    music_string = 'o o| .| o| .| .| .| .| o o'
    notes = parse_music(music_string)
    assert len(notes) == len([4, 2, 1])
```

In this script, the parse_music function uses a dictionary to map music note characters to their respective beat values. The function then uses the string.s matching the pattern to extract the corresponding beats from the music_string. The test_music function tests the validity of the parse_music function by using it to process a sample music_string and checking if the length of the resulting beat list matches the expected length.