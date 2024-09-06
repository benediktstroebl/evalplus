from typing import List
DURATION = {'#': 4, 'o': 1, '|': 2, '.': 1}
def parse_music(music_string: str) -> List[int]:
    result = []
    curr_note = None
    beat = 0

    for c in music_string:
        if c in '.|o|':
            if curr_note is not None:
                result.append(beat)
                beat = 0

            if c == curr_note:
                beat += 1
            else:
                beat = DURATION[c]
            curr_note = c
        elif c == '#':
            result.append(beat)
            beat = 0
            curr_note = None
    # finish the last note
    result.append(beat)
    return result