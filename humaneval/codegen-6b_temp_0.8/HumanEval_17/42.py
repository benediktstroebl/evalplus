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
    result = [0] * len(music_string)
    i = 0
    while i < len(music_string):
        if music_string[i] == 'o':
            for j in range(i, i + 4):
                result[j] += 1
            i += 4
        elif music_string[i] == 'o|':
            for j in range(i, i + 3):
                result[j] += 1
            i += 3
        elif music_string[i] == '.|':
            for j in range(i, i + 2):
                result[j] += 1
            i += 2
        else:
            i += 1
    return result

