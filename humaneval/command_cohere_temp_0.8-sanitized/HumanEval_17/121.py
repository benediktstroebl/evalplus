from typing import List
def parse_music(music_string: str) -> List[int]:
    MOD = 4  # the beat modulo - whole note lasts this many beats
    NOTES = {'o': 4, 'o|': 2, '.|': 1}

    beats = []
    curr_beat = 0
    for note in music_string:
        if note in NOTES:
            curr_beat += NOTES[note]
        else:
            beats.append(curr_beat)
            curr_beat = 0
    beats.append(curr_beat)
    return beats