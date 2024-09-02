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
    music_string = music_string.split(' ')
    music = []

    for i in range(len(music_string)):
        if i % 4 == 0:
            music.append(4)
        elif i % 4 == 1:
            music.append(2)
        elif i % 4 == 2:
            music.append(1)
        elif i % 4 == 3:
            music.append(2)

    return music

