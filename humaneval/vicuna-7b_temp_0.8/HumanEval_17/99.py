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
    note_map = {
        'o': 4,
        'o|': 2,
        '.': 1
    }
    note_list = []
    for note in music_string:
        if note == 'o':
            note_list.append(note_map['o'])
        elif note == '|':
            note_list.append(note_map['o'])
        else:
            note_list.append(note_map[note])
    return note_list

