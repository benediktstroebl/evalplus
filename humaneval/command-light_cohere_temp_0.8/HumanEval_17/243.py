```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o' : 4, 'o|' : 2, '.' : 1, 'o' : 4}
    pattern = r'(?<[\w]+\s+)?(?:\s+[\w]+\s+)?(?=)'
    return [int for int(match[0]) in notes for match in re.search(pattern, music_string)]

def test_parse_music(test_string: str) -> None:
    parsed_notes = parse_music(test_string)
    assert len(parsed_notes) == len(test_string.has_note = False
    for note in test_string.split('\n)[1:]
        if note in 'oooo|oO|.' or in parsed_notes:
            has_note = True
    assert has_note == True
```
The `test_parse_music` function takes a string containing music notes, then splits this string by newline character, and pass this part to the `parse_music` function to parse it. The output of the `parse_music` function will be the list of integers corresponding to how many beats does each note last.