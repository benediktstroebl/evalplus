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

    last_beats = []
    beat_count = 0
    last_beat = 4
    beat_pattern = 'o'
    for character in music_string:
        if character == beat_pattern:
            beat_count += 1
            last_beat = last_beat - 1
        elif character == '|':
            if beat_count > 0:
                last_beats.append(beat_count)
                beat_count = 0
            beat_pattern = 'o'
            last_beat = 4
        elif character == '.':
            last_beat = last_beat - beat_count
            beat_count = 0
            beat_pattern = 'o'
    last_beats.append(beat_count)
    return last_beats

