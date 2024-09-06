from typing import List
PATTERN = {'o': 4, 'o|': 2, '.|': 1}
def parse_music(music_string: str) -> List[int]:
    result: List[int] = []
    curr_beat = 0
    for c in music_string:
        if c in 'o|.|':
            curr_beat += PATTERN[c]
        else:
            result.append(curr_beat)
            curr_beat = 0
    result.append(curr_beat)
    return result