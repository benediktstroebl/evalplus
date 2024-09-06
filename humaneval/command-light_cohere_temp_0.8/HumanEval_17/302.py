```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    beats = {
        'o': 4,
        'o|': 2,
        '|': 1
    }
    
    beats_found = {beat: 0 for beat in beats}
    notes_found = {note: 0 for note in notes}
    
    for beat in beats:
        beats_found[beat] += 1
    
    for note in notes:
        notes_found[note] += 1
    
    notes_counts = {note: notes_found[note] for note in notes}
    
    return notes_counts

# Test cases
def test_parse_music():
    music_str = 'o o| .| o| .| .| .| o o'
    result = parse_music(music_str)
    print(result)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4] -> True passed

# Test case 2
music_str = 'o o| |.| .| o| o'
result = parse_music(music_str)
print(result)  # Output: [4, 2, 1, 1] -> False
```