```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4, 'o|': 2, '|': 1,
        '.': 1, 'oO': 4  # additional test character
    }
    
    beats = [0] * 4
    notes_length = len(music_string)
    
    for i, char in enumerate(music_string):
        beats[i % 4] += notes[char]
    
    return beats

# Example usage:
# Test music_string
music_string = 'o o| .| o| .| .| .| o o'
beats = parse_music(music_string)
print(beats)
```
The solution is a self-contained function that uses a dictionary to map musical notes to the duration of a single beat. It then iterates over the particular notes, and incrementally durations based on the current musical character. The function then returns the result.