from typing import List
def parse_music(music_string: str) -> List[int]:
    beat_mapping = {'o': 4, 'o|': 2, '.': 1}
    notes = []
    curr_beat = 0

    for char in music_string:
        if char in beat_mapping:
            curr_beat += beat_mapping[char]
            notes.append(curr_beat)
        elif char == '|':
            curr_beat = 0

    return notes