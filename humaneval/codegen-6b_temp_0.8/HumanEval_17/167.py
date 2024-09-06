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
    current_chord = []
    for i in range(len(music_string)):
        if music_string[i] == 'o':
            if current_chord:
                result += [pow(2, len(current_chord) - 1)]
            current_chord = []
        elif music_string[i] == 'o|':
            if current_chord:
                current_chord += [1, pow(2, len(current_chord) - 1)]
        elif music_string[i] == '.|':
            if current_chord:
                current_chord += [1, 2, 2, 1, 1, pow(2, len(current_chord) - 1)]
        elif music_string[i] == 'o|o':
            if current_chord:
                current_chord += [1, 2, 2, 1, pow(2, len(current_chord) - 1)]
        else:
            current_chord += [1]

    if current_chord:
        result += [pow(2, len(current_chord) - 1)]
    return result

