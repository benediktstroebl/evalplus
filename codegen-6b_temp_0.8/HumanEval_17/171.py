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
    final = []
    music_string = music_string.split(' ')
    for i in music_string:
        if i == 'o':
            final.append(1)
        elif i == 'o|':
            final.append(1 / 2)
        elif i == '.|':
            final.append(1 / 4)
        elif i == 'o.':
            final.append(1 / 8)
        elif i == '.|.':
            final.append(1 / 16)
        elif i == 'o:':
            final.append(1 / 32)
        elif i == '.|:':
            final.append(1 / 64)
        else:
            final.append(0)
    return final

