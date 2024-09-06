from typing import List
def parse_music(music_string: str) -> List[int]:
    beat_lengths = {
        "o": 4,
        "o|": 2,
        ".|": 1,
    }
    result: List[int] = []
    current_beat = 0

    for char in music_string:
        if char in beat_lengths:
            current_beat += beat_lengths[char]
        else:
            result.append(current_beat)
            current_beat = 0

    # Add last note
    result.append(current_beat)

    return result