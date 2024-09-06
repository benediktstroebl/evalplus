from typing import List
Pattern = str
Beat = int
def parse_music(music_string: Pattern) -> List[Beat]:
    whole_note = 4
    half_note = 2
    quarter_note = 1

    beat_counts: List[Beat] = []
    curr_beat = 0

    for char in music_string:
        if char == "o":
            curr_beat += whole_note
        elif char == "|":
            pass
        elif char == ".":
            beat_counts.append(curr_beat)
            curr_beat = 0
        else:
            raise ValueError(f"Unknown character {char} in music string")

    # finish the last note
    beat_counts.append(curr_beat)

    return beat_counts