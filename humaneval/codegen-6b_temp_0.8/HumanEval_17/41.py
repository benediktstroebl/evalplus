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
    parsed = {}
    for i in music_string.split(" "):
        if not len(i):
            continue
        if i[0] == 'o':
            parsed[1] = 4
        elif i[0] == 'o|':
            parsed[1] = 2
        elif i[0] == '.':
            parsed[1] = 1

        parsed[len(i) - 1] = len(i)

    return [parsed[i] for i in range(max(parsed.keys()), 0, -1)]

