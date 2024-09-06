from typing import List
def parse_music(music_string: str) -> List[int]:
    res = []
    curr_note = 4
    for c in music_string:
        if c == 'o':
            curr_note *= 2
        elif c == '|':
            curr_note //= 2
        elif c == '.':
            res.append(curr_note)
            curr_note = 4
        elif c == ' ':
            continue
        else:
            raise ValueError(f"Unexpected char {c}")
    return res