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
    # Todo: Implement a validator that checks if the music is valid
    music = music_string.split()
    music = ''.join(music)
    music = music.replace('o|', '2').replace('o', '4')
    music = music.replace('.|', '1')
    return list(map(int, music.split('|')))

