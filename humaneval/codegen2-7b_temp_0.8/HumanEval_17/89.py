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
    parsed_music = []
    music_str_list = music_string.split()
    for element in music_str_list:
        if element[-1] == '|':
            parsed_music.append(2)
            element = element[:-1]
        elif element[-1] == '.':
            parsed_music.append(1)
            element = element[:-1]
        else:
            parsed_music.append(4)
    return parsed_
