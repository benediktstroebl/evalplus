from typing import List
def parse_music(music_string: str) -> List[int]:
    mod = 4  # whole note lasts 4 beats
    beats = []

    current_beat = 0
    for char in music_string:
        if char == 'o':
            current_beat += mod
        elif char == 'o|':
            current_beat += mod // 2
        elif char == '.':
            beats.append(current_beat)
            current_beat = 0
        else:
            raise ValueError("Invalid input format!")

    # Finish the last note
    beats.append(current_beat)

    return beats