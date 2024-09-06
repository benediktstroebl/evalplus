```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', 'o.','.'.'.split()  # Get a set of notes is ".", end=''.split('.')
    beat = 4 # whole note is four beats
    beat_half = 2 # half note is two beats

    for note in notes:
        if note == '.' and music_string[0] == 'o':
            start = 1
            beat_count = 0
            for i in range(1, len(music_string)):
                if music_string[i] == '|':
                    beat_count += beat_half
                    if beat_count == beat:
                        start += beat
                        beat_count = 0
                elif music_string[i] == 'o':
                    beat_count += beat
                else:
                    break
            for i in range(start, len(music_string)):
                if music_string[i] == '.':
                    yield beat_count
            yield start
        else:
            start = 1
            beat_count = 0
            for i in range(1, len(music_string)):
                if music_string[i] == '|':
                    beat_count += beat
                    if beat_count == beat:
                        start += beat
                        beat_count = 0
                elif music_string[i] == 'o':
                    beat_count += beat_half
                else:
                    break
            for i in range(start, len(music_string)):
                if music_string[i] == '.':
                    yield beat_count
            yield start
return []
```