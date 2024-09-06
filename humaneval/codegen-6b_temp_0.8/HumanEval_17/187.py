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
    note = ''
    for letter in music_string:
        if letter == ' ':
            if note:
                result.append(len(note))
            note = ''
        elif letter in ['o', 'o|', '.', '|']:
            if note:
                result.append(len(note))
                note = ''
            if letter == 'o':
                result.append(4)
            if letter == 'o|':
                result.append(2)
            if letter == '.':
                result.append(1)
            if letter == '|':
                result.append(0.5)
        else:
            note += letter
    if note:
        result.append(len(note))

    return result

