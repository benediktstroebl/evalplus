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
    res = [int(i) for i in music_string.split()]
    # fill list with o
    if res[0] == 0:
        res = [1] + res
    # fill list with o|
    elif res[0] == 1:
        res = [1, 2] + res
    # fill list with .|
    elif res[0] == 2:
        res = [1, 2, 3] + res

    return res

