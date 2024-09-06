from typing import List
pattern = 'o|_|.'
base_beat = {'o': 4, '|': 2, '._': 1}
def parse_music(music_string: str) -> List[int]:
    result = []
    notes = music_string.strip()
    
    # validate input
    if not set(pattern).issubset(set(notes)):
        raise ValueError("Invalid notes in the string")
    
    for n in notes:
        result.append(base_beat[n])
    return result