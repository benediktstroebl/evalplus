from typing import List
def parse_music(music_string: str) -> List[int]:
    music_string = music_string.strip(' ', '\n')
    return [4 if c == 'o' else 2 if c == 'o|' else 1 for c in music_string.split('|') if c != '']