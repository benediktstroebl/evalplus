from typing import List
def parse_music(music_string: str) -> List[int]:
    mod = 4  # whole note lasts 4 beats
    beat_values = {
        'o': 4, 
        'o|': 2, 
        '.|': 1, 
    }

    result = []
    current_beat = 0
    for note in music_string:
        if note in beat_values:
            current_beat += beat_values[note]
        else:
            result.append(current_beat)
            current_beat = 0 
    # adding the last note
    result.append(current_beat)
    return result