from typing import List
def parse_music(music_string: str) -> List[int]:
    result = []
    curr_note = 4
    for c in music_string:
        if c == 'o':
            result.append(curr_note)
        elif c == '|':
            curr_note //= 2
        elif c == '_':
            curr_note //= 4
        else:
            result.append(curr_note)
    return result