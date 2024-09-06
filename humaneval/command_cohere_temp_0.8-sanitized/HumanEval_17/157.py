from typing import List
def parse_music(music_string: str) -> List[int]:
    beat_conversion = {'o': 4, 'o|': 2, '.': 1}
    result = []
    
    for char in music_string:
        if char in beat_conversion:
            result.append(beat_conversion[char])
    
    return result