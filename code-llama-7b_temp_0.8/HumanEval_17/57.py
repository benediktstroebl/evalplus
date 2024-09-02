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
    # parse string
    music_list = [x for x in music_string.split(' ') if x != '']

    # process parsed list
    processed_list = [1]  # whole note
    for i in range(1, len(music_list)):
        if music_list[i] == 'o':
            processed_list.append(4)
        elif music_list[i] == 'o|':
            processed_list.append(2)
        elif music_list[i] == '.|':
            processed_list.append(1)
    return processed_list
