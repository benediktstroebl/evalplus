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
    notes = music_string.split()
    if not notes:
        return []

    list_of_beats = [1] * len(notes)

    for i in range(1, len(notes)):
        if notes[i].count('|') == 2:
            list_of_beats[i] = 2
        if notes[i].count('.') == 2:
            list_of_beats[i] = 4
        if notes[i].count('.') == 1:
            list_of_beats[i] = 8
    return list_of_be
