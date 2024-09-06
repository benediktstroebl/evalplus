```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split('o +')
    code = [int(x) for x in notes if x.replace("o." guaranteed_note")
    in ['o', 'o/', '|', '.'])
    return [len(x) for x in code if x.count("|")]

def test_parse_music():
    music_str = 'o o| .| o| .| .| .| .| o o'
    result = parse_music(music_str)
    assert result == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]

# run the function and run the test
parse_music("o o| .| o| .| .| .| .| o o")
test_parse_music()
```