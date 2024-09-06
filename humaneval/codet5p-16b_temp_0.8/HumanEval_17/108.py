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

    count = 0
    current_index = 0
    beat_list = []
    while current_index < len(music_string):
        if music_string[current_index] == 'o':
            count = 4
        elif music_string[current_index] == 'o|':
            count = 2
        elif music_string[current_index] == '.':
            count = 1
        else:
            raise ValueError(f'Input string is not valid: {music_string}')
        beat_list.append(count)
        current_index += 1
    return beat_list

