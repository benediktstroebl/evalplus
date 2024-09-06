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
    # your code here
    music = list(music_string)
    while music[0] == 'o' or music[0] == 'o|':
        if music[0] == 'o':
            music.pop(0)
            music.append(4)
        elif music[0] == 'o|':
            music.pop(0)
            music.append(2)
    while music[0] == '.':
        music.pop(0)
        music.append(1)
    # print(music)
    return music

