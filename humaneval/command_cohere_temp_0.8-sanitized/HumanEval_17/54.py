from typing import List
def parse_music(music_string: str) -> List[int]:
    MOD = 4  # the base duration (whole note)
    beat_durations = {'o': 4, 'o|': 2, '.': 1}

    result = []
    current_beat = 0
    for char in music_string:
        current_beat += beat_durations.get(char, 0)
        result.append(current_beat)
        current_beat %= MOD
    return result