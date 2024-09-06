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
    if len(music_string) == 0:
        return []
    result = []
    first_part = music_string.split(' o ')
    for el in first_part:
        if el != '':
            result.append(len(el) // 4)
    second_part = music_string.split(' o| ')
    for el in second_part:
        if el != '':
            result.append(len(el) // 2)
    third_part = music_string.split(' .| ')
    for el in third_part:
        if el != '':
            result.append(len(el) // 0.5)

    return result

