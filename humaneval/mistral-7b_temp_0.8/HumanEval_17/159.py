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
    music = []
    current_length = 4
    for i, char in enumerate(music_string):
        if char == 'o':
            music.append(current_length)
            current_length = 4
        elif char == 'o|':
            music.append(current_length)
            current_length = 2
        elif char == '.':
            music.append(current_length)
            current_length = 1
        elif char == '|':
            music.append(current_length)
            current_length = 1
    return music

