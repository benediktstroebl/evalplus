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
    notes = []
    current_beat = 0
    current_note = 0

    for char in music_string:
        if char == '|':
            if current_note != 0:
                notes.append(current_beat * 4 + current_note)
                current_beat = 0
                current_note = 0
        elif char == 'o':
            current_beat += 1
            current_note += 1
        elif char == '.':
            current_beat += 1
            current_note += 1

    notes.append(current_beat * 4 + current_note)

    return notes
