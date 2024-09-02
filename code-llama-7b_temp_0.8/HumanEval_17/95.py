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
    beats = []
    for index, char in enumerate(music_string):
        if char == 'o':
            if music_string[index+1] == '|':
                beats.append(4)
            else:
                beats.append(4)
                index += 1
        elif char == '.':
            beats.append(1)
        else:
            beats.append(2)
    return beats

