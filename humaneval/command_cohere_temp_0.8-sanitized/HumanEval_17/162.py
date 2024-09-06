from typing import List
def parse_music(music_string: str) -> List[int]:
    durations = []
    curr_beat = 0

    for char in music_string:
        if char == 'o':
            curr_beat += 4
        elif char == '|':
            curr_beat += 2
        elif char == '.':
            durations.append(curr_beat)
            curr_beat = 0
        else:
            raise ValueError(f"Unexpected character '{char}' in the music string.")

    durations.append(curr_beat)

    return durations