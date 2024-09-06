from typing import List
PATTERN = {'o': 4, 'o|': 2, '.': 1}
def parse_music(music_string: str) -> List[int]:
    result = []
    curr_note = 0
    for c in music_string:
        if c in 'o|.":':
            result.append(curr_note)
            curr_note = PATTERN[c]
        else:
            curr_note //= 2
    result.append(curr_note)
    return result