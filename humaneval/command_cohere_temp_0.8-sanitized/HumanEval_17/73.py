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

    MOD = 4  # the beat modulo, whole note lasts this many beats
    NOTES = {'o': 4, 'o|': 2, '.|': 1}

    beat_counts = []
    curr_beat = 0

    for note in music_string:
        if note in NOTES:
            beat_counts.append(curr_beat)
            curr_beat = (curr_beat + NOTES[note]) % MOD
        elif note == '|':
            curr_beat = (curr_beat + 1) % MOD
        elif note == '.':
            curr_beat = (curr_beat + 1) % MOD

    beat_counts.append(curr_beat)

    return beat_counts