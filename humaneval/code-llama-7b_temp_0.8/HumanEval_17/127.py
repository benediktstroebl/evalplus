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
    beats = [4, 2, 1]
    result = []
    music_string = music_string.split(' ')
    for i in range(len(music_string)):
        if music_string[i] == 'o':
            result.append(beats[0])
        elif music_string[i] == 'o|':
            result.append(beats[1])
        elif music_string[i] == '.|':
            result.append(beats[2])
        elif i < len(music_string) - 1 and music_string[i] == '.|.' and music_string[i + 1] == '.|':
            result.append(beats[2] * 3)
        elif i < len(music_string) - 1 and music_string[i] == '.|.' and music_string[i + 1] == '.|.':
            result.append(beats[2] * 2)
        elif i < len(music_string) - 1 and music_string[i] == 'o|' and music_string[i + 1] == 'o|':
            result.append(beats[1] * 3)
        elif i < len(music_string) - 1 and music_string[i] == 'o|' and music_string[i + 1] == 'o':
            result.append(beats[0] * 3)
        elif i < len(music_string) - 1 and music_string[i] == 'o|' and music_string[i + 1] == '.|':
            result.append(beats[0] + beats[1])
    return result

