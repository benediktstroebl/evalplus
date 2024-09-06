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
    whole_note = 4
    half_note = 2
    quater_note = 1

    music_list = music_string.split()

    beats_list = []
    for element in music_list:
        if 'o' in element:
            beats = whole_note
        elif '|' in element:
            beats = half_note
        else:
            beats = quater_note
        beats_list.append(beats)
    return beats_list

