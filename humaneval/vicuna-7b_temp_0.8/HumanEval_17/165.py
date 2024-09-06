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
    last_note = True
    current_beat = 1
    for char in music_string:
        if char == 'o':
            beats.append(current_beat)
            if last_note:
                last_note = False
                current_beat += 1
        elif char == '|':
            last_note = not last_note
            current_beat += 1
        elif char == '.' and last_note:
            beats.append(current_beat)
            current_beat += 1
            last_note = not last_note
    return beats