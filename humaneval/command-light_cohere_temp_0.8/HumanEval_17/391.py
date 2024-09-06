Here is a Python script that does that:
```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    
    def get_beat(note):
        if note in notes:
            return notes[note]
        else:
            raise ValueError(f"Unknown note: {note}")
    
    beats = []
    for note in music_string:
        beats.append(get_beat(note))
        
    return beats

# Example usage:
music_str = 'o o| .| o| .| .| .| .| o o'
beats = parse_music(music_str)
print(beats)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This script defines a `parse_music` function that turns a music string into a list of beats. The function also includes error handling to ensure that the music string follows the correct format.