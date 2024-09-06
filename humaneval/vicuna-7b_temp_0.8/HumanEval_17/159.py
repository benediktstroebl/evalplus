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
    note_type = "o"
    for char in music_string:
        if char == note_type:
            beats.append(0)
        elif char == 'o':
            note_type = "o"
            beats.append(0)
        elif char == '|':
            note_type = "|"
            beats[-1] += 2  # half note is lasting twice as long as a whole note
        else:
            note_type = "."
            beats[-1] += 1  # quater note is lasting twice as long as a half note
    beats.append(0)
    return beats