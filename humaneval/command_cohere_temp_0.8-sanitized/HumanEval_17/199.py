from typing import List
def parse_music(music_string: str) -> List[int]:
    result = []
    beats = 4
    for note in music_string.strip():
        if note == 'o':
            result.append(beats)
        elif note == '|':
            beats //= 2
        else:
            beats //= 4
    return result