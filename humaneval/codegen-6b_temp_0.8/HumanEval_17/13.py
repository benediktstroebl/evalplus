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
    result = [0] * len(music_string)

    beats_cnt = 0
    current_interval = 4
    for index in range(len(music_string)):
        if index + current_interval >= len(music_string):
            break
        if music_string[index] == 'o':
            result[index] = 0
        elif music_string[index] == 'o|' and music_string[index + 1] == 'o':
            result[index] = 1
            result[index + 1] = 1
            current_interval = 1
        elif music_string[index] == 'o' and music_string[index + 1] == 'o|':
            result[index + 1] = 0
            result[index] = 1
            current_interval = 1
        elif music_string[index] == 'o' and music_string[index + 1] == 'o':
            result[index] = 1
            current_interval = 1
        elif music_string[index] == 'o' and music_string[index + 1] == 'o|':
            result[index] = 1
            current_interval = 1
        elif music_string[index] == 'o' and music_string[index + 1] == 'o':
            result[index] = 1
            current_interval = 1
        elif music_string[index] == 'o' and music_string[index + 1] == 'o|':
            result[index] = 1
            result[index + 1] = 1
            current_interval = 1
        elif music_string[index] == 'o' and music_string[index + 1] == 'o':
            result[index + 1] = 0
            result[index] = 1
            current_interval = 1
        elif music_string[index] == 'o' and music_string[index + 1] == 'o|':
            result[index] = 1
            result[index + 1] = 1
            current_interval = 1
        elif music_string[index] == 'o' and music_string[index + 1] == 'o|':
