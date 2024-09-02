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
    if music_string == "":
        return []

    result = [0] * 12

    for beat in music_string.split():
        if "|" in beat:
            result[0] = beat.count("|") + result[0]
            result[-1] = beat.count("|") + result[-1]
            result.pop()
            continue
        if "." in beat:
            result[-1] = beat.count(".") + result[-1]
            result.pop()
            continue
        result[beat] += 1

    return result

