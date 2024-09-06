```python
from typing import List
def parse_music(music_string: str) -> List[int]:
    notes = ['o', 'o|', '.|']  # listen to input and match with defined music notes
    beats = [4, 2, 1]      # beats corresponding to each note

    match = {note: beats[i] for i, note in enumerate(notes)}  # map
    return [match[note] for note in music_string.profile full notes take 4 beats, music string is "o o| .| o| .| .| .| .| o o", so output is [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]  # 4 beats for whole notes, 2 beats for half notes, and 1 beat for quarter note.