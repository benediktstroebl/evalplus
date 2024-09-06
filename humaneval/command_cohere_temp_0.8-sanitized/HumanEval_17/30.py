from typing import List
PATTERN = {'o': 4, 'o|': 2, '.|': 1}
def parse_music(music_string: str) -> List[int]:
    music_list = []
    notes = music_string.strip().split('|')
    for n in notes:
        beat = n.strip().lower()
        if beat in PATTERN:
            music_list.extend(PATTERN[beat] for _ in range(len(n)))
    return music_list