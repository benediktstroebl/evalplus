from typing import List
def parse_music(music_string: str) -> List[int]:
    beat_dict = {'o': 4, 'o|': 2, '.': 1}
    beats = []

    cur_beat = 0
    for char in music_string:
        if char in beat_dict:
            cur_beat += beat_dict[char]
            beats.append(cur_beat)
            cur_beat = 0
    # Add remaining beat
    if cur_beat > 0:
        beats.append(cur_beat)

    return beats