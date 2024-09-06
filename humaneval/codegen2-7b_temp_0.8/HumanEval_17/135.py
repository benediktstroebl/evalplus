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
    for index, char in enumerate(music_string):
        if char == 'o' or char == '.':
            parsed.append(4)
        elif char == 'o' or char == '|':
            parsed.append(2)
        elif char == '.' or char == '|':
            parsed.append(1)
        else:
            raise ValueError(f"Unable to parse music string {music_string} at index {index}.")
    return parsed

