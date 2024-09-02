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
    parse = music_string.split()
    if parse[-1] == '|':
        parse = parse[:-1]
    res = []
    for i in parse:
        if i == 'o':
            res.append(4)
        elif i == '.':
            res.append(1)
        else:
            res.append(int(i[1:]))
    return res

