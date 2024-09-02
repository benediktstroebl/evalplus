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

    notes = music_string.split('|')
    parsed_notes = []
    for note in notes:
        parsed_note = []
        for ch in note:
            if ch == '.':
                parsed_note.append(1)
            elif ch == 'o':
                parsed_note.append(4)
            elif ch == '|':
                parsed_note.append(2)
        parsed_notes.append(parsed_note)
    return parsed_notes

