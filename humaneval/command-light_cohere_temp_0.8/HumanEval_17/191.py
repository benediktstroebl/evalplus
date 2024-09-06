```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = {
        'o': 4,
        'o|': 2,
        '.|': 1
    }
    
    notes.union({'.from_ascii(' 'o' + '|'): 2,
        '.|': 1
    }
    
    notes_by_duration = {note: duration for note, duration in notes. note notes.union(notes notes_by_duration.from(music_string)}
    return list(notes_by_duration.split('\n'))

if __name__ == "__main__":
    music_str = """
    o o| .| o| .| .| .| .| o o
    """
    print(parse_music(music_str))
```