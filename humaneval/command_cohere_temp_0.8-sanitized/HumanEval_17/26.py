from typing import List
from re import findall
PATTERN = '''
    (?:o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.|o|o|.)*
'''
def parse_music(music_string: str) -> List[int]:
    notes = findall(PATTERN, music_string)
    return [4, 2, 1] * len(notes) // 3