```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(" "). music_string.split(' ')
   I
    /'\nOutput:   )/midi_notes
    return midi_notes
def test_parse_music(test_string: str) -> None:
    parsed_notes = parse_music(test_string)
    if not parsed_notes:
        print("Error: test_string was not successfully parsed.")
    return parsed_notes == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
#Example usage:
test_string = "o o| .| o| .| .| .| .| o o"
test_parse_music(test_string)
```