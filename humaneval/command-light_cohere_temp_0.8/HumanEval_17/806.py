```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']
    beat_length = [4, 2, 1]

    def get_beat_length(note):
        for b in beat_length:
            if note.startswith(b):
                return b
        return 0

    notes = [note for note in notes if note in music_string]
    beat_note = get_beat_length(music_string[0])

    beats = [0]
    for note in notes:
        beats += get_beat_length(note)
        music_string = music_string[1:] + note + music_string[2:]
        if music_string[-1] != '.':
            beats += beat_length[-1]
        music_string = music_string[0:-1] + music_string[-1] + '.'

    return beats

# Example tests
print(parse_music('o o| .| o| .| .| .| .| o o'))  # [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
print(parse_music('.'))  )  # []
print(parse_music('oo.'))  )  # [0]
print(parse_music('o o o|.'))  # [4, 4]
```
This script defines a function `parse_music` that parses a given music string and returns the total number of beats in the music. The function uses a legend of notes, and beat lengths.