from typing import List
def parse_music(music_string: str) -> List[int]:
    MOD = 4  # the base duration (whole note) lasts this many beats

    beat_list = []
    curr_beat = 0

    for c in music_string:
        if c == 'o':
            beat_list.append(curr_beat)
            curr_beat = 0
        elif c == 'o|':
            curr_beat += 2
        elif c == '.':
            curr_beat += 1
        else:
            # should never happen
            beat_list.append(curr_beat)

    beat_list.append(curr_beat)

    return beat_list