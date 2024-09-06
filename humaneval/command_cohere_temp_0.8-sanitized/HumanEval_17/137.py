from typing import List
def parse_music(music_string: str) -> List[int]:
    beat_mapping = {'o': 4, 'o|': 2, '.': 1}
    parsed_beats = []
    current_beat = 0

    for char in music_string:
        current_beat += beat_mapping.get(char, 0)
        parsed_beats.append(current_beat)
        current_beat = 0

    # Add remaining current beat
    if current_beat > 0:
        parsed_beats.append(current_beat)

    return parsed_beats