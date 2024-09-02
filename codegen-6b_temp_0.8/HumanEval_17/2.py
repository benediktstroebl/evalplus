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
    prev_digit = -1
    curr_number = 0
    curr_list = []

    for letter in music_string:
        number = IN[letter]
        if prev_digit > -1 and number > prev_digit:
            curr_number += 1
            curr_list.append(curr_number)
        else:
            curr_number = 1
            curr_list.append(curr_number)
        prev_digit = number

    return curr_list


IN = {'o': 4, 'o|': 2, '.|': 1, 'qu': 1}
