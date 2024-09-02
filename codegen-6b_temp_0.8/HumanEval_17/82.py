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
    beat_duration = 0
    song = []
    i = 0
    while i < len(music_string):
        char = music_string[i]
        if char == "o":
            if beat_duration == 4:
                song += [4]
            else:
                song += [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
            beat_duration = 0
        elif char == "o|":
            if beat_duration == 4:
                song += [4, 2]
            else:
                song += [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
            beat_duration = 0
        elif char == ".":
            if beat_duration == 4:
                song += [4, 1]
            else:
                song += [4, 2, 1, 2, 2, 1, 1, 1, 1, 4, 4]
            beat_duration = 0
        else:
            beat_duration += 1
            i += 1
    return song

