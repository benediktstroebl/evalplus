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
    list_of_vals = []
    for i in music_string.split(' '):
        if i == 'o' or i == 'o|':
            list_of_vals += [1]
        elif i == '.|':
            list_of_vals += [0.5]
        elif i == 'o|o':
            list_of_vals += [0.25]
        elif i == '.|o':
            list_of_vals += [0.125]
        elif i == 'o|o|':
            list_of_vals += [0.0625]
        elif i == '.|o|':
            list_of_vals += [0.03125]
        elif i == 'o|o|o':
            list_of_vals += [0.015625]
        elif i == '.|o|o':
            list_of_vals += [0.0078125]
    return list_of_vals

