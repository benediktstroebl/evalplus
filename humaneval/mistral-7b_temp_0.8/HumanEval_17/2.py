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
    parsed = []
    for i in range(0, len(music_string)):
        if music_string[i] == '|':
            if i < len(music_string)-1 and music_string[i+1] == '.':
                parsed.append(1)
            elif i < len(music_string)-1 and music_string[i+1] == 'o':
                parsed.append(2)
            elif i < len(music_string)-1 and music_string[i+1] == '|':
                parsed.append(4)
            else:
                return None
        elif music_string[i] == 'o':
            parsed.append(4)
        elif music_string[i] == '.':
            parsed.append(1)
    return parsed
