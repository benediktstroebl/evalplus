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
    total_length = 0
    notes = []
    for n in music_string.split():
        if n not in 'o|.|' and n != 'o':
            notes.append(4)
        elif n == 'o':
            total_length += 1
        elif n == 'o|':
            total_length += 1 / 2
        elif n == 'o|.':
            total_length += 1 / 4
            total_length += 1
        elif n == 'o|o':
            total_length += 1 / 4
            total_length += 1 / 2

    return total_length

