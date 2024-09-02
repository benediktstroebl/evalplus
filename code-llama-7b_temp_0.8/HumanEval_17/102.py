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
    whole_note = 4
    half_note = 2
    quarter_note = 1
    result = []
    if not music_string:
        return result
    string_list = music_string.split(' ')
    for note in string_list:
        if note == 'o':
            result.append(whole_note)
        elif note == 'o|':
            result.append(half_note)
        elif note == '.|':
            result.append(quarter_note)
    return result

