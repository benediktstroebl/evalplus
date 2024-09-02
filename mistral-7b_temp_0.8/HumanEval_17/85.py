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
    state = 'o'
    for i, char in enumerate(music_string):
        if char == '|':
            if state == 'o':
                notes.append(4)
            elif state == 'o|':
                notes.append(2)
            else:
                notes.append(1)
            state = '.'
        else:
            if state == 'o':
                notes.append(4)
            elif state == 'o|':
                notes.append(2)
            else:
                notes.append(1)
            state = char
    return notes

