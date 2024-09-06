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

    if not music_string:
        return []
    output_list = []
    current_duration = 0
    for note in music_string.split(' '):
        if note == 'o':
            current_duration += 4
        elif note == 'o|':
            current_duration += 2
        elif note == '.':
            current_duration += 1
        elif note == '|':
            output_list.append(current_duration)
            current_duration = 0
        elif note == 'o o':
            output_list.append(current_duration)
            output_list.append(current_duration)
            current_duration = 0
    return output_list

