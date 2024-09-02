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
    if not music_string:
        return parsed

    while music_string:
        current_note = music_string[0]
        if current_note == 'o':
            parsed.append(4)
        elif current_note == 'o|':
            parsed.append(2)
        elif current_note == '.|':
            parsed.append(1)

        music_string = music_string[1:]

    return parsed

