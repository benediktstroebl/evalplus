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
    beats_lasted = []
    multiplier = 1
    for char in music_string:
        if char == 'o':
            beats_lasted.append(4 * multiplier)
        elif char == 'o|':
            beats_lasted.append(2 * multiplier)
        elif char == '.|':
            beats_lasted.append(1 * multiplier)
        elif char == ' ':
            multiplier *= 2
    return beats_lasted

