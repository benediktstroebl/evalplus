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

    for note in music_string:
        # if the current character is an 'o'
        if note == 'o':
            # return the number of beats it lasts
            beats = 4
        # if the current character is 'o|'
        elif note == 'o|':
            # return the number of beats it lasts
            beats = 2
        # if the current character is '.|'
        elif note == '.|':
            # return the number of beats it lasts
            beats = 1
        # otherwise, assume the character is a quarter note
        else:
            beats = 1

        result.append(beats)

    return result
