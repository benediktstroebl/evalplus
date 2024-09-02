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
    current_beat = 0
    for note in music_string:
        # 1. check if note is 'o'
        if note == 'o':
            beats.append(current_beat)
            current_beat += 4
        # 2. check if note is '|'
        elif note == '|':
            # move the current beat pointer to next note
            current_beat += 2
        # 3. check if note is '.', ',' or '.'
        elif note in ['.', ',', '.']:
            # move the current beat pointer to next note
            current_beat += 1
        # 4. check if note is 'o'
        elif note == 'o':
            beats.append(current_beat)
            current_beat += 4
    return beats
