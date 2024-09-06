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
    beat = 0
    beats = []
    for ch in music_string:
        if ch == 'o':
            beat += 4
        elif ch == '.':
            beat += 1
        elif ch == '|':
            if beat == 2:
                beat += 1
        beats.append(beat)
    return beats

