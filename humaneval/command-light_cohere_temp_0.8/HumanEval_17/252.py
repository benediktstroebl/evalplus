```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {'o': 4, 'o|': 2, '.|': 1}
    
    beat_lengths = {note: length for note, length in notes.  }
    notes.
    
    return [ Music music_string.split('|')[:-1]  # Left-strip off the bar character
    beat_counts = {length: count for length, count in beat_lengths.

    beats = [map(lambda x: int(x) - 1, beat_counts. For -1 because the value of an empty string).

# Example usage
music_str = 'o o| .| o| .| .| .| .| o o'
notes = parse_music(music_str)
print(notes)
```