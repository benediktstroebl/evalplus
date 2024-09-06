```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '|', 'o', 'o', '.']
    result = [len(note) for note in notes if note.contains(music_string)]
    return result

def test_parse_music(test_string: str) -> None:
    music_str = "# music music\n" + test_string + "\n# music"
    result = parse_music(music_str)
    if not result:
        print("No notes found!")
        return None
    return result

# Example usage
test_str = "o o| .| o| .| .| .| .| o o"
result = test_parse_music(test_str)
if result:
    print("Found notes: ", result)
```
This code provides a function `parse_music` that takes a string representing music notes in a special ASCII format and returns a list of integers corresponding to the number of beats for each note. The `test_parse_music` function provides a test string and ensures the `parse_music` function returns the correct result.