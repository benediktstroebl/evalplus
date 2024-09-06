from typing import List
def parse_music(music_string: str) -> List[int]:
    mod = 4  # whole note lasts 4 beats
    beat_map = {
        'o': 4,
        'o|': 2,
        '.|': 1,
    }
    result: List[int] = []
    current_beat = 0

    for char in music_string:
        current_beat += beat_map.get(char, 0)
        result.append(current_beat)
        current_beat %= mod  # ensure that the beat counter is reset to 0 for each new beat
    return result