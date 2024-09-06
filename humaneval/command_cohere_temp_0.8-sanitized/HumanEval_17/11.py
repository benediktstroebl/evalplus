from typing import List
def parse_music(music_string: str) -> List[int]:
    beat_count = {'o': 4, '^': 2, '.': 1}
    return [beat_count[char] for char in music_string] if music_string else []