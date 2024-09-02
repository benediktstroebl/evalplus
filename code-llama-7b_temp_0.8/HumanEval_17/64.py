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
    # convert music string to list
    music_list = list(music_string.replace(" ", ""))
    # list with result
    result_list = []
    for n in music_list:
        if n == "o":
            result_list.append(4)
        elif n == "o|":
            result_list.append(2)
        elif n == ".|":
            result_list.append(1)

    return result_list

