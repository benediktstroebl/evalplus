from typing import List
def parse_music(music_string: str) -> List[int]:
    beat_mapping = {'o': 4, 'o|': 2, '.|': 1}
    parsed_beats = []
    current_beat = 0

    for char in music_string:
        current_beat += beat_mapping.get(char, 0)
        parsed_beats.append(current_beat)
        current_beat -= 1  # To account for the fact that a whole note counts as 4 beats, not 5

    return parsed_beats