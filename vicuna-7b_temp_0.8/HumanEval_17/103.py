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
    current_beat = 0
    for char in music_string:
        if char == 'o':
            if current_beat % 4 == 0:
                result.append(4)
            result.append(current_beat)
            current_beat += 4
        elif char == '|':
            if current_beat % 2 == 0:
                result.append(2)
            result.append(current_beat)
            current_beat += 2
        else:
            if current_beat % 1 == 0:
                result.append(1)
            result.append(current_beat)
            current_beat += 1
    return result