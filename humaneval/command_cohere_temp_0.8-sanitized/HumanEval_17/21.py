from typing import List
def parse_music(music_string: str) -> List[int]:
    beat_count = []
    cur_beat = 4

    for note in music_string.strip():
        if note == 'o':
            beat_count.append(cur_beat)
        elif note == '|':
            cur_beat //= 2
        elif note == '.':
            beat_count.append(cur_beat // 4)
        cur_beat //= 4

    return beat_count