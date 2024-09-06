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
    patterns = ('.|', 'o|', 'o o|')
    output = []
    current_index = 0
    while current_index < len(music_string):
        for pattern in patterns:
            if music_string[current_index:current_index + len(pattern)] == pattern:
                output.append(len(pattern) - 1)
                current_index += len(pattern)
                break
        else:
            raise ValueError('Unable to parse music string')
    return output

