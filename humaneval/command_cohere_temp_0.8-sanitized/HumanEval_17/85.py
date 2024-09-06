from typing import List
beats = {'o': 4, 'o|': 2, '.|': 1}
def parse_music(music_string: str) -> List[int]:
    result = []
    notes = music_string.strip().split('|')
    for n in notes:
        result.extend([beats[x] for x in n if x in beats])
    return result