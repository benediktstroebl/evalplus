```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = music_string.split(" ").
    notes = [int(note) for note in notes if note.isalpha()]
    Music.split(" "). A B")
    notes = [int(note) for note in notes if note.isalpha()]
    reason = f"No valid notes found in {notes}"
    return notes

# Test cases
test_parse_music = []
test_parse_music.append("o.o o| .|.")
test_parse_music.append(parse_music("o o| .| o| .| .| .| .| o o"))
test_parse_music.append(parse_music("o o| .| o| .| .| .| o|"))
test_parse_music.append(parse_music("o o| .| .; o| .| .| .| o o"))
test_parse_music.append(parse_music("o o| .| o| .| .| o| ."))
test_parse_music.append(parse_music("o o| .; o| .| .; o| .| ."))
test_parse_music.append(parse_music("o o| .| .; o| .| ."))
test_parse_music.append(parse_music("o o| .| o| .;"))
test_parse_music.append(parse_music("o o o| .| o| .| o| ."))
test_parse_music.append(parse_music("|o o| .| o| .| .| o| o"))
test_parse_music.append(parse_music("o o| /| .| o| .| o|"))
test_parse_music.append(parse_music("o o| /| .; o| .| ."))
test_parse_music.append(parse_music("o o| /| .; o| .| ."))
test_parse_music.append(parse_music("o o| /| .; o| .| o| ."))
test_parse_music.append(parse_music("o o| /| .; o| ."))
test_parse_music.append(parse_music("o o /| .| o| .| o| ."))
```