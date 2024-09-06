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
    for i, note in enumerate(music_string):
        if note == 'o':
            result.append(1)
        elif note == 'o|':
            result.append(0.5)
        elif note == ''.join('o|' * 2):
            result.append(0.25)
        elif note == ''.join('o|' * 3):
            result.append(0.125)
    return result

