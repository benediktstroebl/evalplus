from typing import List
def parse_music(music_string: str) -> List[int]:
    result = []
    current_note = 4
    
    for char in music_string:
        if char == 'o':
            current_note *= 2
        elif char == '|':
            current_note //= 2
        elif char == '.':
            result.append(current_note)
            current_note = 4
        else:
            raise ValueError(f"Unknown character {char} found in music string")
    
    # Process the rest of the melody
    result.append(current_note)
    
    return result