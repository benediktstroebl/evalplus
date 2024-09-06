from typing import List
def parse_music(music_string: str) -> List[int]:
    NOTES = {'o': 4, 'o|': 2, '.': 1}
    return [NOTES.get(note, 1) for note in music_string.strip()]