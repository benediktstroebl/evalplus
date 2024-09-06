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
    rests = []
    curr_note = 0

    for i in music_string:
        if i == 'o':
            curr_note += 4
        elif i == 'o|':
            curr_note += 2
        elif i == '.':
            curr_note += 1
        elif i == '|':
            notes.append(curr_note)
            rests.append(4)
            curr_note = 0

    if curr_note:
        notes.append(curr_note)
        rests.append(4)

    return [x + y for x, y in zip(notes, rests)]

