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
    parsed_music = [0] * len(music_string)
    current_note = 0

    for i in range(1, len(music_string)):
        note = music_string[i]
        if note == '|':
            current_note = current_note + 1
        elif note == '.':
            parsed_music[current_note] = parsed_music[current_note] + 1
            current_note = current_note + 1
        else:
            current_note = current_note + 2
    return parsed_
