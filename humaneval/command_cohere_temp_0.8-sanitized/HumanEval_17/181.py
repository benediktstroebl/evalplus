from typing import List
def parse_music(music_string: str) -> List[int]:
    beat_lengths = {'o': 4, 'o|': 2, '.|': 1}
    result = []
    current_beat = 0

    for note in music_string:
        if note in beat_lengths:
            current_beat += beat_lengths[note]
        else:
            result.append(current_beat)
            current_beat = 0

    # Handle the last note
    result.append(current_beat)

    return result