from typing import List
def parse_music(music_string: str) -> List[int]:
    mod = 4  # whole note lasts 4 beats
    beat_values = {
        'o': 4, 
        'o|': 2, 
        '.|': 1, 
        '|': 0, 
        '.': 0, 
    }
    res = []
    curr_beat = 0
    for note in music_string:
        if note in beat_values:
            curr_beat += beat_values[note]
        else:
            curr_beat = 0
        res.append(curr_beat)
    return res