from typing import List
def parse_music(music_string: str) -> List[int]:
    beat_lengths = {'o': 4, 'o|': 2, '.|': 1}
    result = []
    
    for note in music_string.strip():
        if note in beat_lengths:
            result.append(beat_lengths[note])
        else:
            result.append(0)
    
    return result