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

    # print(music_string)
    # print(type(music_string))
    # print(len(music_string))
    # print(music_string[1])
    # print(music_string.split())
    # print(len(music_string.split()))
    # print(len(music_string.split()[1]))
    # print(music_string.split()[1][0])
    # print(music_string.split()[1][1])
    # print(music_string.split()[1][1][0])
    # print(music_string.split()[1][1][0].isalpha())
    # print(music_string.split()[1][1][0].isdigit())
    # print(music_string.split()[1][1][1])
    # print(music_string.split()[1][1][1].isalpha())
    # print(music_string.split()[1][1][1].isdigit())

    # 1. Write a regular expression to identify each
