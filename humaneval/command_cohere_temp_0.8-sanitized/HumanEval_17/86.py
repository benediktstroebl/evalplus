from typing import List
def parse_music(music_string: str) -> List[int]:
    mod = 4  # whole note lasts 4 beats
    beat_values = {
        'o': 4, 
        'o|': 2, 
        '.|': 1
    }

    result: List[int] = []
    current_beat = 0

    for char in music_string:
        current_beat += beat_values.get(char, 0)
        result.append(current_beat)
        current_beat %= mod  # ensure that the result is cyclic (e.g. 'o o| .| o| o| .| .| .| o o' result is [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4])

    return result