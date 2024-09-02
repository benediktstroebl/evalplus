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
    final_list = []
    if not isinstance(music_string, str):
        return []

    if not music_string:
        return []

    for i in range(0, len(music_string), 1):
        if music_string[i] == 'o':
            final_list.append(4)
        elif music_string[i] == 'o|':
            final_list.append(2)
        elif music_string[i] == 'o|o':
            final_list.append(1)
        elif music_string[i] == 'o|o|':
            final_list.append(0.5)
        elif music_string[i] == 'o|o|o':
            final_list.append(0.25)

    return final_list

