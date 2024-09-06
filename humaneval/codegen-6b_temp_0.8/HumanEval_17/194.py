from typing import List


def parse_music(music_string: str) -> List[int]:
    """ Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return list of integers corresponding to how many beats does each
    not last.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    >>> parse_music('o o| .| o| o| .| .| .| .| o o')
    [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
    """
    res = []
    last_beat_number = -1
    full_bars = 0
    for c in music_string:
        if c == 'o':
            res.append(1)
        elif c == 'o|':
            res.append(1 / 2)
        elif c == '.|':
            res.append(1 / 4)
        else:
            res.append(0)

        if c == 'o' or c == 'o|' or c == 'o|':
            last_beat_number += 1
        elif c == '.' or c == 'o':
            last_beat_number = 0

        if c == 'o' and last_beat_number == 0:
            full_bars += 1

    res.append(full_bars)

    return res

