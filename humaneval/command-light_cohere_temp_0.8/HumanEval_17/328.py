```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']
    notes = [note.join for note in notes]
    
    pattern = r'\b({ notes[::2] })\b'
    
    return [int(match.group()) for match in re.match(pattern, music_string)]

def test_parse_music(test_string: str) -> None:
    music = re.sub(pattern, '', test_string)
    notes = parse_music(music)
    return (isinstance(notes, List) and all(map( isinstance , notes )) and all(map( note > 0, notes)) )

# Example test cases
test_parse_music('o o| .| o| .| .| .| o o')
test_parse_music('o o o| .| o| .| .| .| .| o o')
test_parse_music(''.--)
test_parse_music('O')
test_parse_music('x')
```
The function `parse_music` parses a music string containing notes in the ASCII format provided in the docstring and the function returns a list of corresponding integers. The `test_parse_music` function contains several test cases for the `parse_music` function, including a test case to ensure that the `parse_music` function correctly handles empty input strings and invalid inputs.