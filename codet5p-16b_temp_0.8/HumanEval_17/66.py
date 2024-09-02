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

    result = []
    length = len(music_string)
    i = 0
    while i < length:
        if music_string[i] == 'o':
            result.append(4)
            i += 1
        elif music_string[i:i + 2] == 'o|':
            result.append(2)
            i += 2
        elif music_string[i:i + 2] == '.|':
            result.append(1)
            i += 2
        else:
            raise ValueError(f'Unknown note: {music_string[i]}')
    return result
