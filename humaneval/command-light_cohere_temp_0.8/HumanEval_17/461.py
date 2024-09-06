```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    
    beat_counts = {
        'o': 4,
        'o|': 2,
        '|': 1,
    }

    def get_beat_count(note):
        return beat_counts.get(note, 1)
    
    notes_with_beats = {note: get_beat_count(note) for note in notes.
    notes = {k: v for k, v in notes_with_beats.items() if k in music_string}
    
    return [int(note) for note in notes.

# Example usage
music_str = 'o o| .| o| .| .| .| .| o o'
result = parse_music(music_str)
print(result)  # Output: [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```