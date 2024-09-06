```python
from typing import List

def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']  # legend of note lengths
    note_lengths = {note: 4 for note in notes}  # map of note to length

    beats = music_string.split(' ')'.

    beat_lengths = [int(len(beat) / 4) for beat in beats.

    return [ [note_lengths.setdefault(note_lengths)][: len(beats)]  # Convert legend and beat length pairs into a list of beat lengths

    return beats
```
This function takes a string music_string, which represents a sequence of notes with their lengths in the musical format. The function then splits the music_string by ' ', extracting all the beat lengths, and then maps the legend of note lengths to the beat length. The function returns a list of beat lengths.