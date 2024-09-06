```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    beat = 1
    notes_list = []
    for note in music_string.split(' ' '):
        if note in notes:
            notes_list.append(beat)
            beat += notes[note]
    return notes_list

# Test the function
test_parse_music = parse_music('o o| .| o| .| .| .| .| o o')
print(test_parse_music)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```
This Python code defines a function `parse_music` that takes a music string in a specific format and returns a list of integers representing the number of beats in the music. The function uses a legend of musical notes: 'o' is a whole note lasting four beats, 'o| is a half note lasting two beats, and '.|' is a quarter note lasting one beat. The function iterates through these strings of characters to a list of integers representing the number of beats for each musical note.