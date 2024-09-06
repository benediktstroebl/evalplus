from typing import List
pattern = 'o|_|.'
base_beat = {'o': 4, '|': 2, '._': 1}
def parse_music(music_string: str) -> List[int]:
    music_list = [base_beat[char] for char in music_string if char in pattern]
    return [beat * num for beat, num in zip(music_list, range(len(music_list), 0, -1))]