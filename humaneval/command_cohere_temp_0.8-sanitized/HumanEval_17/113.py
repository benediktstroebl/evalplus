from typing import List
base_beat = {'o': 4, '|': 2, '._': 1}
def parse_music(music_string: str) -> List[int]:
    result = []
    notes = music_string.strip(' o|_|.')
    for n in notes:
        result.append(base_beat[n])
    return result