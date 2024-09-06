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
    list_of_notes = music_string.split()
    list_of_beats = [0] * len(list_of_notes)
    for i, x in enumerate(list_of_notes):
        if x == 'o':
            list_of_beats[i] = 4
        elif x == 'o|':
            list_of_beats[i] = 2
        elif x == '.|':
            list_of_beats[i] = 1
        else:
            list_of_beats[i] = -1
    return list_of_beats

