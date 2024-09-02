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

    output = []
    beats_left = 4
    current_beat = 0
    for char in music_string:
        if char == 'o':
            beats_left = 4
            output.append(beats_left)
        elif char == 'o|':
            beats_left = 2
            output.append(beats_left)
        elif char == '.':
            beats_left = 1
            output.append(beats_left)
        elif char == '|':
            output.append(current_beat)
            current_beat = 0
        else:
            current_beat += 1
    return output

