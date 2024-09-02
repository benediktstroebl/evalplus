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
    note_map = {
        'o': 4,
        '|': 2,
        '\\': 1
    }
    for note in music_string:
        if note == 'o':
            # if note is 'o' then add 4 beats to the list
            beats.append(4)
        elif note == '\\':
            # if note is '\\' then move to next line and reset the beats count
            beats = []
        else:
            # if note is not 'o' or '\\' then it is a note
            # use note map to determine number of beats
            beats.append(note_map[note])
    return beats

