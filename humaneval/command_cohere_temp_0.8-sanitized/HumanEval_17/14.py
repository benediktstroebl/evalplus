from typing import List
def parse_music(music_string: str) -> List[int]:
    result = []
    notes = music_string.strip().split('|')
    beat_pattern = {
        'o': 4,
        '|': 2,
        '^': 1,
        '.': 1
    }

    for n in notes:
        count = len(n) * beat_pattern[n[0]]
        result.append(count)

    return result