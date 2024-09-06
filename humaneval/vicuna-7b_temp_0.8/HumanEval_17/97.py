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
    beats = [0] * 12
    for note in music_string:
        if note == 'o':
            beats[0] += 1
            beats[1] += 1
            beats[2] += 1
        elif note == 'o|':
            beats[3] += 1
            beats[4] += 1
        elif note == '.':
            beats[5] += 1
        elif note == '|':
            beats[6] += 1
            beats[7] += 1
    return beats