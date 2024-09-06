from typing import List
def parse_music(music_string: str) -> List[int]:
    beats = []
    for i, char in enumerate(music_string):
        if char == 'o':
            beats.append(4)
        elif char == '|':
            beats.append(2)
        elif char == '.':
            beats.append(1)
        else:
            raise ValueError(f"Invalid input. Char '{char}' is not supported.")
    return beats