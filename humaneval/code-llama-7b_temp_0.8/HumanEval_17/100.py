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
    last_char = music_string[0]
    # each char must be in 'o.|'
    for current_char in music_string[1:]:
        if last_char == 'o' and current_char == 'o':
            result.extend([4, 4])
        elif last_char == 'o' and current_char == '|':
            result.append(4)
        elif last_char == 'o' and current_char == '.':
            result.append(1)
        elif last_char == '.' and current_char == 'o':
            result.extend([4, 4])
        elif last_char == '.' and current_char == '|':
            result.append(2)
        elif last_char == '.' and current_char == '.':
            result.append(1)
        elif last_char == '|' and current_char == 'o':
            result.append(4)
        elif last_char == '|' and current_char == '|':
            result.append(2)
        elif last_char == '|' and current_char == '.':
            result.append(1)
        else:
            raise ValueError("Invalid notation. Use 'o', '.', '|' only")
        last_char = current_char
    return result

