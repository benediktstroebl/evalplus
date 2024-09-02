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
    beats = [0] * 10
    index = 0
    while index < len(music_string):
        if music_string[index] == 'o':
            beats[0] += 1
        elif music_string[index] == 'o|':
            beats[0] += 2
        elif music_string[index] == '.':
            beats[0] += 1
        index += 1
    return beats

