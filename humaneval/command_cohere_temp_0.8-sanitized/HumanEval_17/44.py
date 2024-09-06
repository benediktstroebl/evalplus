from typing import List
PATTERN = {'o': 4, 'o|': 2, '.|': 1}
def parse_music(music_string: str) -> List[int]:
    music_list = []
    beat = 0
    
    for char in music_string:
        if char in 'o|.|':
            beat += PATTERN[char]
        else:
            beat //= 2
        music_list.append(beat)
    
    return music_list