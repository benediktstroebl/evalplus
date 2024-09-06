from typing import List
def parse_music(music_string: str) -> List[int]:
    MOD = 4  # the base duration (whole note)
    beat_durations = {'o': 4, 'o|': 2, '.|': 1}

    result = []
    current_beat = 0
    for char in music_string:
        if char in beat_durations:
            current_beat += beat_durations[char]
            result.append(current_beat)
        else:
            current_beat = (current_beat + MOD) % MOD
    return result