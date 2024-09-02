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
    return_list = []
    beats = 0
    for char in music_string:
        if chars.isspace(char) or char == 'o':
            beats += 1
            if beats % 4 == 0 and not char == 'o':
                return_list.append(4)
                beats = 0
        if char == 'o':
            return_list.append(4)
            beats = 0
        elif char == 'o|':
            return_list.append(2)
            beats = 0
        elif char == '.|':
            return_list.append(1)
            beats = 0
        elif char == 'o':
            return_list.append(4)
            beats = 0
        elif char == '|':
            beats = 0
        elif char == '.':
            beats = 0
        else:
            return_list.append(0)
            beats = 0
    return return_list


chars = [' ', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o',
         'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o',
         'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o',
         'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o', 'o