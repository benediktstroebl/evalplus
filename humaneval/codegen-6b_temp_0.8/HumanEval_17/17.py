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
    res = []
    i = 0
    while i < len(music_string):
        while i < len(music_string) and music_string[i] == ' ':
            i += 1
        if i >= len(music_string):
            return res
        if music_string[i] == 'o':
            res.append(4)
            i += 1
        elif music_string[i] == 'o|':
            res.append(2)
            i += 1
        elif music_string[i] == 'o|':
            res.append(2)
            i += 1
        elif music_string[i] == 'o|':
            res.append(2)
            i += 1
        elif music_string[i] == 'o|':
            res.append(2)
            i += 1
        elif music_string[i] == 'o|':
            res.append(2)
            i += 1
        elif music_string[i] == 'o|':
            res.append(2)
            i += 1
        elif music_string[i] == 'o|':
            res.append(2)
            i += 1
        elif music_string[i] == 'o|':
            res.append(2)
            i += 1
        elif music_string[i] == 'o|':
            res.append(2)
            i += 1
        elif music_string[i] == 'o|':
            res.append(2)
            i += 1
        elif music_string[i] == 'o|':
            res.append(2)
            i += 1
        elif music_string[i] == 'o|':
            res.append(2)
            i += 1
        elif music_string[i] == 'o|':
            res.append(2)
            i += 1
        elif music_string[i] == 'o|':
            res.append(2)
            i += 1
        elif music_string[i] == 'o|':
            res.append(2)
            i += 1
        elif