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
    music_string = music_string.replace("_", " ")
    music_list = music_string.split()
    music_list = [x[:-1] if x[-1] == "|" else x for x in music_list]
    music_list = [int(x[1]) if x[0] == "o" else 0.5 if x[0] == "|" else 0.25 for x in music_list]
    return music_list

