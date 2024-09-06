from typing import List
Pattern = str
Notes = List[int]
def parse_music(music_string: Pattern) -> Notes:
    beat = 4
    notes = []
    parts = music_string.split('|')
    for n in parts:
        if 'o' == n:
            notes.append(beat)
        elif '.' != n:
            notes.append(int(n[1]) * beat)
        beat //= 2
    return notes