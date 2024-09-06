```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '|': 1}
    notes_in_music = music_string.split('o first music_string')[1:-1]
    return [notes[note] for note in notes_in_music]

# Test cases
def test_parse_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    expected = [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    actual = parse_music(music_str)
    assert actual == expected

# Run the function and test it
test_parse_music()
```
This Python script defines a function `parse_music` that takes a music string in a specific format and returns a list of integers corresponding to the number of beats in each note. The function uses a legend:
- `o`: Whole note, lasting four beats
- `o|`: Half note, lasting two beats
- `|`: Quarter note, lasting one beat

The function splits the music string into a list of characters, excluding the final newline character, and then uses a dictionary to map these characters to the respective beat values.

Finally, the script provides a test case that checks if the `parse_music` function correctly returns the expected output for a given music string.