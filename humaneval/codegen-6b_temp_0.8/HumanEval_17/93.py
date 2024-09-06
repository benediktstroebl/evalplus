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
    pos = 0
    while pos < len(music_string):
        # next char is any of o.
        if (pos + 1) < len(music_string) and music_string[pos] == music_string[pos + 1]:
            pos += 2
        else:
            pos += 1
        res.append(1)
    return res

