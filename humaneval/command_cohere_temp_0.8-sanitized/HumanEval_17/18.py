from typing import List
pattern = 'o|^.<|o|O|.|o|'
def parse_music(music_string: str) -> List[int]:
    dw = {'o': 4, 'O': 4, '|': 1, '^': 2, '.': 1}
    el = music_string.strip(pattern).split(pattern)
    return [dw[el[i]] * len(el[i]) for i in range(len(el))]