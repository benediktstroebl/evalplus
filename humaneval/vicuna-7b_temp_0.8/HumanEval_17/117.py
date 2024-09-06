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
    note = ''
    last_beat = None
    for char in music_string:
        if char == 'o':
            if last_beat is not None:
                beats.append(last_beat)
                last_beat = None
            beats.append(1)
            note = 'o'
        elif char == '|':
            if note == 'o':
                last_beat = '1' if last_beat is None else '0'
                beats.append(last_beat)
                last_beat = None
            else:
                last_beat = '1' if last_beat is None else '0'
                beats.append(last_beat)
                last_beat = None
            note = '|'
        elif char == '.':
            if note == 'o':
                last_beat = '1' if last_beat is None else '0'
                beats.append(last_beat)
                last_beat = None
            else:
                last_beat = '1' if last_beat is None else '0'
                beats.append(last_beat)
                last_beat = None
            note = '.'
        else:
            raise ValueError("Invalid character in music string")
    if note == 'o':
        if last_beat is not None:
            beats.append(last_beat)
            last_beat = None
        beats.append(1)
    beats.append(1)
    return beats

