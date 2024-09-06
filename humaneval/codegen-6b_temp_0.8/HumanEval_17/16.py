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
    for note in music_string.split():
        if note == 'o':
            result.extend(['o'] * 4)
        elif note == 'o|':
            result.extend(['o', 'o'])
        elif note == 'o|o':
            result.extend(['o', 'o', 'o', 'o'])
        elif note == 'o|o|':
            result.extend(['o', 'o', 'o', 'o'])
        elif note == 'o|o|o':
            result.extend(['o', 'o', 'o', 'o', 'o', 'o'])
        elif note == '.|':
            result.extend(['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'])
        elif note == '|':
            result.extend(['o', 'o'])
        elif 'o|o|' in note:
            parts = note.split('o|')
            result.extend(['o'] * int(parts[0]) + ['o', 'o'] * int(parts[1]))
        elif 'o|' in note:
            parts = note.split('o|')
            result.extend(['o'] * int(parts[0]) + ['o'] * int(parts[1]))
    return result

