from typing import List
PATTERN = {'o': 4, 'o|': 2, '.': 1}
def parse_music(music_string: str) -> List[int]:
    result: List[int] = []
    curr_beat = 0

    for char in music_string:
        if char in 'o|.":':
            curr_beat += PATTERN[char]
        else:
            result.append(curr_beat)
            curr_beat = 0

    # Last chunk
    result.append(curr_beat)

    return result