from typing import List
def parse_music(music_string: str) -> List[int]:
    beat_dict = {'o': 4, 'o|': 2, '.': 1}
    beats = []

    for char in music_string:
        if char in beat_dict:
            beats.append(beat_dict[char])
        else:
            beats.append(0)

    return beats