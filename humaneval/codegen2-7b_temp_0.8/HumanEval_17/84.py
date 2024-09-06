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
    note = ""
    for char in music_string:
        if char == 'o':
            if note!= "":
                result.append(4 - len(note))
            note = ""
        elif char == '.':
            result.append(4 - len(note))
            note = ""
        else:
            if char == '|':
                note += '|'
            elif char == 'o':
                note += 'o'
            else:
                raise ValueError('Invalid note.')
    if note!= "":
        result.append(4 - len(note))
    return
