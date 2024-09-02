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
    parsed_music = music_string.split()

    total_length = 0
    for line in parsed_music:
        current_length = 0
        for letter in line:
            if letter == 'o':
                current_length += 4
            elif letter == 'o|':
                current_length += 2
            elif letter == '.' or letter == '|':
                current_length += 1
        total_length += current_length
    return [total_length // 4] * len(parsed_music)

