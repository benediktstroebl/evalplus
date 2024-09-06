Here's a solution:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = music_string.split('|')
    for note in notes:
        note = note.strip(). differntype(note)
        if note != '':
            raise ValueError("Invalid note format")
        beat = 4 if note[0] == 'o' else 2 if note[0] == '|' else 1
        yield beat

# Test the function with a string that passes the test
test_music = "o o| .| o| .| .| .| .| o o"
result = parse_music(test_music)
print(result)  # This should print [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This function splits the input string by '|', which is used to indicate a change in pitch, and yields the beat count of each note. It then extracts whole notes ('o') and half notes ('o|') which last 2 beats and quarter notes '.|' which last 1 beat.  The valid note formats, it raises a ValueError with an appropriate message.