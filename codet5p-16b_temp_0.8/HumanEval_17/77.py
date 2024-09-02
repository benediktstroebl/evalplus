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

    beats: List[int] = []
    current_beat: int = 0
    note: str = ''

    for char in music_string:
        if char == 'o':
            current_beat += 4
        elif char == 'o|':
            current_beat += 2
        elif char == '.|':
            current_beat += 1

        if char!= '.' and char!= '|':
            note += char
        else:
            beats.append(current_beat)
            current_beat = 0
            note = ''

    if note:
        beats.append(current_beat)

    return beats

