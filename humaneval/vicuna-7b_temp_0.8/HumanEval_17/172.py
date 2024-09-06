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
    music = music_string.strip().split('|')
    beats = [0] * len(music)
    for i in range(len(music)):
        note, rest = music[i], music[i+1:]
        if note == 'o':
            beats[i] += 4
        elif note == '|':
            beats[i] += 2
        else:
            beats[i] += 1
    return beats

