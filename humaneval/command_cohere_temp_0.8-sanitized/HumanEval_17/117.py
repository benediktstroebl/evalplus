from typing import List
pattern = 'o|_|.'
base_beat = {'o': 4, '|': 2, '_': 1, '.': 0}
def parse_music(music_string: str) -> List[int]:
    result = []
    notes = music_string.strip()
    
    # check if there is a valid note at each position
    for char in notes:
        if char not in pattern:
            raise ValueError("Invalid note")
            
    # iterate through the string and count beats accordingly
    for i, char in enumerate(notes):
        result.append(base_beat[char])
    
    return result