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
    beats = []
    last_beat = False
    for char in music_string:
        if char == 'o':
            beats.append(4)
            last_beat = False
        elif char == '|':
            beats.append(2)
            last_beat = False
        elif char == '.':
            beats.append(1)
            last_beat = False
        elif char == 'o' and last_beat == False:
            last_beat = True
        elif char == '|' and last_beat == True:
            last_beat = False

    return beats