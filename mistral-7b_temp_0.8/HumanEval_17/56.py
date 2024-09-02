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
    output = []
    count = 0
    is_whole = False

    for symbol in music_string:
        if symbol == 'o':
            if is_whole:
                count += 4
            else:
                count += 2
                is_whole = True
        elif symbol == '|':
            if is_whole:
                count += 4
                is_whole = False
            else:
                count += 1
        else:
            output.append(count)
            count = 0
    output.append(count)
    return output

