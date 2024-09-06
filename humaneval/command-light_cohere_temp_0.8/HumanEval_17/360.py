```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']
    notes_lengths = [4, 2, 1]
    
    for note, length in zip(notes, notes_lengths):
        if note in music_string:
            index = music_string.find(note)
            assert index != -1, f"Error: {note} not found in {music_string}"
            yield index

# Test code
test_parse_music = []
test_parse_music.insert("o string = "o o| .| o| .| .| .| o o")
test_parse_music.insert(parse_music(" ".join(string)))
test_parse_music.insert(parse_music("Invalid"))
test_parse_music.insert(parse_music("Invalid"))
print("test_parse_music:", test_parse_music)
```