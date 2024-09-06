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
    beats = 0
    note_count = {}
    note_type = []
    for char in music_string:
        if char == 'o':
            beats += 1
            note_count['whole'] += 1
            if len(note_count) > 20:
                note_count.pop(note_count.keys()[0])
        elif char == '|':
            note_count['half'] += 1
        elif char == '|':
            note_count['quarter'] += 1
    for char in music_string:
        if char == '.':
            note_count['eighth'] += 1
        elif char == ':':
            note_count['sixteenth'] += 1
            beats += 1
    return beats

