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
    music_notes = music_string.split()
    beat_list = []
    for note in music_notes:
        if note == 'o':
            beat_list.extend([4])
        elif note == 'o|':
            beat_list.extend([2])
        elif note == '.|':
            beat_list.extend([1])
    return beat_list

