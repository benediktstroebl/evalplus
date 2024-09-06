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
    current = 0
    is_half_note = False
    is_quater_note = False
    for char in music_string:
        if char =='':
            if is_quater_note:
                is_quater_note = False
                is_half_note = True
                current = 0
            elif is_half_note:
                is_half_note = False
                is_quater_note = True
                current = 0
        else:
            current += 1
            if current == 4:
                result.append(1)
                current = 0
    return result + [1] * (4 - len(result
