from typing import List
def parse_music(music_string: str) -> List[int]:
    beat_map = {'o': 4, 'o|': 2, '.|': 1}
    beats = []
    
    current_beat = 0
    for note in music_string:
        if note in beat_map:
            current_beat += beat_map[note]
        else:
            beats.append(current_beat)
            current_beat = 0
    
    beats.append(current_beat)
    return beats