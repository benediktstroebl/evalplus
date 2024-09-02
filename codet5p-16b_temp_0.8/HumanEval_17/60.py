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

    note_duration = 0

    for i, c in enumerate(music_string):
        if c == 'o':
            note_duration += 4
        elif c == 'o|':
            note_duration += 2
        elif c == '.':
            note_duration += 1

        if i!= len(music_string)-1 and music_string[i+1] == '|':
            result.append(note_duration)
            note_duration = 0

    return result
