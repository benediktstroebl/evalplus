from typing import List
def parse_music(music_string: str) -> List[int]:
    mod = 4  # whole note lasts 4 beats
    beat_values = {
        'o': 4, 
        'o|': 2, 
        '.|': 1
    }    
    
    result = []
    curr_beat = 0
    
    for char in music_string:
        if char in beat_values:
            curr_beat += beat_values[char]
        else:
            result.append(curr_beat)
            curr_beat = 0
    
    # finish the last sequence
    result.append(curr_beat)
    
    return result