from typing import List
def parse_music(music_string: str) -> List[int]:
    result = []
    current_note = 4
    for char in music_string:
        if char in 'o|.":':
            current_note *= 2 if char in 'o:' else 1
        elif char == '|':
            current_note //= 2
        result.append(current_note)
    return result