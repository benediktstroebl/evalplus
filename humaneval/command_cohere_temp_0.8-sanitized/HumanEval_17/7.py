from typing import List
def parse_music(music_string: str) -> List[int]:
    result = []
    curr_note = 4

    for c in music_string:
        if c == 'o':
            curr_note *= 4
        elif c == '|':
            curr_note //= 2
        elif c == '.':
            result.append(curr_note)
            curr_note = 4
        else:
            raise ValueError(f"Unexpected char `{c}` in the music string")

    if curr_note != 4:
        result.append(curr_note)

    return result