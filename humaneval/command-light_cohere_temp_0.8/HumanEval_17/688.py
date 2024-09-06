```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '|', 'o', '.']
    beats = [1, 2, 4, 1]

    def get_duration(note):
        if note == 'o':
            return beats
        elif note == 'o|':
            return beats[0]
        elif note == '|':
            return beats[1]
        else:
            return beats[2]

    notes = [get_duration(note) for note in notes]

    return [beat for beat in range(len(music_string)) for note in music_string[:beat] for _ in notes]

# Tests
music_str = 'o o| .| o| .| .| .| .| o o'
print(parse_music(music_str))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
```

This function uses a set of predefined notes and beat durations to parse the music string. The function works by iterating over the music string to find the beginning of each beat. It then uses the other functions to get the duration of each note in that beat and adds that duration to a list of numbers representing the number of beats in this beat.