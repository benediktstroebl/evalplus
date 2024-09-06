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

    if music_string.count('|') > 4:
        raise ValueError('Each note must be specified at most 4 times')
    if music_string.count('|') == 0:
        return [4]
    if music_string.count('|') == 1:
        return [2, 2]
    if music_string.count('|') == 2:
        return [1, 2]
    if music_string.count('|') == 3:
        return [1, 1, 2]
    if music_string.count('|') == 4:
        return [1, 1, 1, 1]
    return [4]
