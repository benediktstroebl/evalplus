from typing import List
def parse_music(music_string: str) -> List[int]:
    MOD = 4  # the base duration (whole note) lasts this many beats

    beat_count = []
    curr_beat = 0

    for c in music_string:
        if c == 'o':
            curr_beat += MOD
        elif c == 'o|':
            curr_beat += MOD // 2
        elif c == '.':
            beat_count.append(curr_beat)
            curr_beat = 0
        else:
            beat_count.append(curr_beat)

    return beat_count