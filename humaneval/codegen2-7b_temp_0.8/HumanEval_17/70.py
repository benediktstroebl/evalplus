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
    res = []
    prev_bpm = 0
    prev_beat = 0
    prev_beat_type = ""
    for c in music_string:
        bpm = int(c[0])
        beat_type = c[1]
        beat_count = int(c[2])
        if prev_bpm!= bpm:
            prev_bpm = bpm
            prev_beat = beat_count
        if beat_type!= prev_beat_type:
            prev_beat_type = beat_type
            res.append(beat_count - prev_beat)
    return res

