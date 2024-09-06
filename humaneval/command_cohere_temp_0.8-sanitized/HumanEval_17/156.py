from typing import List
def parse_music(music_string: str) -> List[int]:
    LEG = ['o', 'o|', '.|']
    res = []
    beat = 4
    for n, char in enumerate(music_string):
        if char in LEG:
            res.append(beat)
            if char == 'o|':
                beat = 2
            elif char == '.|':
                beat = 1
        else:
            beat //= 2
    return res