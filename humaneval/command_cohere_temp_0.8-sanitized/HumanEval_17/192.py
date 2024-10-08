from typing import List
def parse_music(music_string: str) -> List[int]:
    beat_map = {'o': 4, 'o|': 2, '.|': 1}
    result = []
    
    current_beat = 0
    for char in music_string:
        current_beat += beat_map.get(char, 0)
        result.append(current_beat)
    
    return result