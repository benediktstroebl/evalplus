from typing import List
pattern = 'o|_|.'
def parse_music(music_string: str) -> List[int]:
    Beats = ['o', '|', '.']
    result = []
    
    for i in range(len(music_string)):
        if music_string[i] in pattern:
            result.append(Beats.index(music_string[i]))
    
    return result