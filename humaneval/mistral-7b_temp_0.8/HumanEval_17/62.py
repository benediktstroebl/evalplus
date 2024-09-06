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
    parse_result = []
    current_note_number = 0
    current_note_duration = 0
    for i in range(len(music_string)):
        if music_string[i] == 'o':
            current_note_duration = 4
            current_note_number += 1
        elif music_string[i] == '|':
            if music_string[i - 1] == '.':
                current_note_duration = 1
            else:
                current_note_duration = 2
            current_note_number += 1
        elif music_string[i] == '.':
            current_note_duration = 1
            current_note_number += 1
        parse_result.append(current_note_duration)
    return parse_result
