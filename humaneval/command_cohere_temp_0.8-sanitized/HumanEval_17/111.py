from typing import List
def parse_music(music_string: str) -> List[int]:
    beat_dict = {'o': 4, 'o|': 2, '.': 1}
    beats = []
    
    current_beat = 0
    for char in music_string:
        if char in beat_dict:
            current_beat += beat_dict[char]
        else:
            beats.append(current_beat)
            current_beat = 0
    
    # Handle the last note
    beats.append(current_beat)
    return beats