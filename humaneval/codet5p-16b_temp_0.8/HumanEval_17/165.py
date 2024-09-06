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

    return_list = []
    index = 0
    while index < len(music_string):
        if music_string[index] == 'o':
            return_list.append(4)
            index += 1
        elif music_string[index] == 'o|':
            return_list.append(2)
            index += 1
        elif music_string[index] == '.|':
            return_list.append(1)
            index += 1
        else:
            return_list.append(music_string[index])
            index += 1
    return return_list

