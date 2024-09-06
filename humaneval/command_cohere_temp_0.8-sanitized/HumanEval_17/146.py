from typing import List
def parse_music(music_string: str) -> List[int]:
    res = []
    cur_beat = 4
    for note in music_string:
        if note == 'o':
            res.append(cur_beat)
        elif note == '|':
            cur_beat //= 2
        elif note == '.':
            res.append(cur_beat // 4)
        cur_beat //= 4
    return res