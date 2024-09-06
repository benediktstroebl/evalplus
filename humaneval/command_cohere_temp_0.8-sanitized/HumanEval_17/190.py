from typing import List
def notes_to_beat(char: str) -> int:
    beat = {'o': 4, 'o|': 2, '.|': 1, '_': 0}
    return beat.get(char, 0)
def parse_music(music_string: str) -> List[int]:
    beats = []
    notes = music_string.strip(' ')
    for i in notes:
        if i == '|':
            beats.append(0)
        else:
            beats.append(notes_to_beat(i))
    return beats