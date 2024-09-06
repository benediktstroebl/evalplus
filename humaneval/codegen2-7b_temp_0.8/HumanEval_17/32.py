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
    beat_list = []
    curr_beat = 0
    for index, character in enumerate(music_string):
        if character == '|':
            curr_beat += 1
        elif character == 'o':
            beat_list.append(curr_beat)
            curr_beat = 0
        elif character == '.':
            curr_beat += 1

    if curr_beat > 0:
        beat_list.append(curr_beat)
    return beat
