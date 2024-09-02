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
    note_map = {'o': 4, '|': 2, '.' : 1}
    beats = []
    current_beat = 0
    current_note = ''
    for char in music_string:
        if char == 'o':
            current_note += 'o'
            beats.append(current_beat)
            current_beat += 4
        elif char == '|':
            current_note += '|'
            beats.append(current_beat)
            current_beat += 2
        elif char == '.':
            current_note += '.'
            beats.append(current_beat)
            current_beat += 1
        elif char == 'm':
            if current_note == 'm':
                raise ValueError("Invalid notation in music string")
            current_note += 'm'
            current_beat = 1
        elif char == '#':
            if current_note == 'm':
                current_note = ''
                current_beat = 1
            elif current_note == 'o':
                current_note = ''
                current_beat = 4
            elif current_note == '|':
                current_note = ''
                current_beat = 2
            elif current_note == '.':
                current_note = ''
                current_beat = 1
        else:
            raise ValueError("Invalid character in music string")
    return beats
