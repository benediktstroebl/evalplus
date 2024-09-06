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
    current = 0
    while current < len(music_string):
        n = music_string[current]
        if n == 'o':
            res.append(4)
            current += 1
        elif n == 'o|':
            res.append(2)
            current += 2
        elif n == '.':
            res.append(1)
            current += 1
        else:
            res.append(1)
            current += 3
    return res
