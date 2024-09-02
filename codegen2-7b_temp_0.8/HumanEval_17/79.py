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
    notes = music_string.split()
    beats = [0] * len(notes)
    for i in range(len(notes) - 1):
        if notes[i][-1] == "|":
            if notes[i + 1][0] == ".":
                beats[i] = 1
                beats[i + 1] += 1
            else:
                beats[i] = 2
                beats[i + 1] += 2
        else:
            beats[i] = 4
    return beats

