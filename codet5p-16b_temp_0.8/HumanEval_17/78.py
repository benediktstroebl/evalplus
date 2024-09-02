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
    current_time = 0
    for note in music_string:
        if note == 'o':
            output.append(4)
            current_time = 4
        elif note == 'o|':
            output.append(2)
            current_time = 2
        elif note == '.':
            output.append(1)
            current_time = 1
        elif note == '|':
            output.append(current_time)
            current_time = 0
        else:
            print('Wrong input. Try again.')
    return output

