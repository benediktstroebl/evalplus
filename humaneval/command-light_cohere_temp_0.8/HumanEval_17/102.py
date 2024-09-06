```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split('o

    notes_list = []
    for note in notes:
        if note.count("oes"):
            note = int(note)  # Convert to integer
        notes_list.append(note)
        else:
            notes_list.append(4)  # Assign default value of 4 if it doesn't match any regex

    return notes_list

# Example usage of function with tests
test_parse_music = []
test_parse_music.append("o" "o o| .| o| .| .| .| .| o o")
test_parse_music.append(parse_music.extract_notes([4, 2, 1, 2, 2, 1, 1, 1, 1, 1, 4, 4] ))
test_parse_music.append(parse_music.extract_notes([4, 2, 1, 2, 2, 1, 1, 1, 1, 1, 4]))
print(test_parse_music.all [x])
```
Do you need help with anything else?