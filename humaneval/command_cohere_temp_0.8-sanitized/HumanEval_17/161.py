from typing import List
def parse_music(music_string: str) -> List[int]:
    beat_map = {'o': 4, 'o|': 2, '.': 1}
    return [beat_map[note] for note in music_string.strip()]