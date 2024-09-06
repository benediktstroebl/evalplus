from typing import List
def parse_music(music_string: str) -> List[int]:
    result = []
    curr_note = 4
    for char in music_string:
        if char == 'o':
            result.append(curr_note)
        elif char == '|':
            curr_note //= 2
        elif char == '.':
            curr_note //= 4
        else:
            raise ValueError(f"Unexpected character {char} found!")
    return result