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
    current_note_length = 1
    for letter in music_string:
        if letter == 'o':
            current_note_length += 1
            if current_note_length == 4:
                current_note_length = 1
        elif letter == 'o|':
            current_note_length += 1
            if current_note_length == 2:
                current_note_length = 1
        elif letter == '.|':
            current_note_length = 1
        elif letter == '|':
            if current_note_length > 1:
                current_note_length -= 1
        if current_note_length != 1:
            result.append(current_note_length)
    return result

