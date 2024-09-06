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

    music_notes = music_string.split('|')
    res = []
    for music_note in music_notes:
        if len(music_note) == 0:
            continue
        else:
            if music_note[-1] == '.':
                res.append(4)
            elif music_note[-1] == 'o':
                res.append(4)
            elif 'o' in music_note[-1]:
                res.append(2)
            else:
                res.append(1)
    return res
