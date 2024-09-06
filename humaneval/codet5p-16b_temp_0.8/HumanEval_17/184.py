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

    return []
    # pass
    notes = []
    current_note = 0
    for c in music_string:
        if c == 'o':
            current_note += 4
        elif c == 'o|':
            current_note += 2
        elif c == '.':
            current_note += 1
        else:
            raise Exception(f'Unknown symbol {c} in string')
        notes.append(current_note)
    return notes
    # TODO: implement this function
    pass

