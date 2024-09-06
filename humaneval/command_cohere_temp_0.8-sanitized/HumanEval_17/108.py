from typing import List
def parse_music(music_string: str) -> List[int]:
    result = []
    curr_beat = 4
    for c in music_string:
        if c == 'o':
            result.append(curr_beat)
        elif c == '|':
            curr_beat /= 2
        elif c == '.':
            result.append(1)
        else:
            raise ValueError(f"Unexpected character {c} found in music string")
    return result