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
    string_list = music_string.split()
    music_list = []
    for idx in range(0, len(string_list), 2):
        note = string_list[idx]
        value = int(string_list[idx + 1])
        if note == 'o':
            music_list.extend([value] * 4)
        if note == 'o|':
            music_list.extend([value] * 2)
        if note == '.':
            music_list.extend([value] * 1)

    return music_list

