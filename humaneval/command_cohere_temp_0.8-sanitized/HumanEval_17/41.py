from typing import List
pattern = 'o|_|.'
beats = {
    'o': 4,
    '|': 2,
    '._': 1,
}
def parse_music(music_string: str) -> List[int]:
    music_list = [beats[char] for char in music_string if char in pattern]
    return music_list