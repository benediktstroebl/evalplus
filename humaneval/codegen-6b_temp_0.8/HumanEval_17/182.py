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
    start = 0
    while start < len(music_string):
        part = music_string[start]
        value = 0
        if part == 'o':
            value = 4
        elif part == 'o|':
            value = 2
        elif part == '.':
            value = 1
        res.append(value)
        start += 1
    return res

