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
    result = []

    if not music_string:
        return result

    last_char = None
    current = 0
    for c in music_string:
        if c == 'o':
            current += 1
        elif c == 'o|':
            current += 2
        elif c == '.':
            current += 4
        elif c == 'o|.':
            result.append(1)
            result.append(2)
            result.append(4)
            current += 2
        elif c == '.':
            result.append(4)
            current += 4
        else:
            result.append(current)

    return result


assert parse_music('o o| .| o| o| .| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
assert parse_music('o o| .| o| o| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 4, 4]
assert parse_music('o o| o| o| o| o o') == [8, 4, 2, 1, 2, 1, 1, 2, 4, 4]
assert parse_music('o o| .| o| o| .| o.| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
assert parse_music('o o| .| o| o| .| .| .| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
assert parse_music('o .| o.| o o| o| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 4, 4]
assert parse_music('o .| o.| o o| o| o o') == [4, 2, 1, 2, 2, 1, 1, 1, 4, 4]
assert parse_music('o o o| .| o o') == [8, 4, 2, 1, 2, 1, 1, 2, 4, 4]
assert