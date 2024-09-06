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
    counter = 0
    result = []
    for i in music_string:
        if i == 'o':
            counter += 1
        elif i == 'o|':
            counter = counter / 2
        elif i == '.':
            counter = counter / 4
        elif i == '|':
            counter = 1
        result.append(counter)
    return result

