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

    notes = []

    current_note = ''
    for char in music_string:
        if char == 'o':
            current_note += '4'
        elif char == 'o|':
            current_note += '2'
        elif char == '.|':
            current_note += '1'
        else:
            notes.append(int(current_note))
            current_note = ''

    notes.append(int(current_note))

    return notes

