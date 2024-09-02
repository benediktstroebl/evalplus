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
    note_count = 0
    last_note = True
    for char in music_string:
        if char == 'o':
            beats.append(note_count)
            note_count = 0
            last_note = True
        elif char == '|':
            note_count = 0
            last_note = not last_note
        elif char == '.' and not last_note:
            beats.append(note_count)
            note_count = 0
            last_note = True
        elif char == '.' and last_note:
            beats.append(note_count)
            note_count = 0
            last_note = False
        else:
            raise ValueError('Invalid music string format')
    return beats