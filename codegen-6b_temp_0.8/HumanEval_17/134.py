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
    beat_counter = 0
    for char in music_string:
        if char == 'o':
            beats.append(beat_counter)
            beat_counter = 0
        elif char == 'o|':
            beat_counter += .5
        elif char == '.|':
            beat_counter += .25
        else:
            beat_counter += 1
    return beats

