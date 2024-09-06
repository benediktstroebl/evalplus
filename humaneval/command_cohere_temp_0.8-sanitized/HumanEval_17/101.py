from typing import List
def parse_music(music_string: str) -> List[int]:
    result = []
    curr_beat = 4
    for note in music_string:
        if note == 'o':
            result.append(curr_beat)
        elif note == '|':
            curr_beat //= 2
        elif note == '.':
            result.append(1)
        else:
            result.append(0)
    return result