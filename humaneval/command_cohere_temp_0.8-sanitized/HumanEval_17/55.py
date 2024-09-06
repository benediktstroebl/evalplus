from typing import List
def parse_music(music_string: str) -> List[int]:
    beat_mapping = {'o': 4, 'o|': 2, '.': 1}
    beats = []

    current_beat = 0
    for char in music_string:
        if char in beat_mapping:
            current_beat += beat_mapping[char]
            beats.append(current_beat)
            current_beat = 0
    # Add remaining current beat
    beats.append(current_beat)
    return beats