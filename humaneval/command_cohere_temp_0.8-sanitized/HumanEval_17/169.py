from typing import List
beats = {'o': 4, 'o|': 2, '.': 1}
def parse_music(music_string: str) -> List[int]:
    result = []
    notes = music_string.strip().split('|')
    for n in notes:
        result.extend([beats[c] for c in n if c in beats])
    return result