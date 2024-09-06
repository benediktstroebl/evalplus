from typing import List
def parse_music(music_string: str) -> List[int]:
    res = []
    curr_beat = 4
    for note in music_string:
        if note == 'o':
            res.append(curr_beat)
        elif note == '|':
            curr_beat //= 2
        elif note == '.':
            res.append(curr_beat // 4)
        curr_beat //= 4
    return res