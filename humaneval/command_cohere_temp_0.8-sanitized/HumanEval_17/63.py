from typing import List
def parse_music(music_string: str) -> List[int]:
    beat_mapping = {'o': 4, 'o|': 2, '.': 1}
    parsed_beats = []
    notes = music_string.split('|')
    
    for i, note in enumerate(notes):
        beat = sum(beat_mapping[char] for char in note if char in beat_mapping)
        parsed_beats.extend([beat] * (i + 1))
    
    return parsed_beats