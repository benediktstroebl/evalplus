from typing import List, Optional
def parse_music(music_string: str) -> List[int]:
    beat_dict = {'o': 4, 'o|': 2, '.|': 1}
    beats = []

    cur_beat = 0
    current_note = None  # Optional[str]

    for note in music_string:
        if current_note is None:
            if note in beat_dict:
                current_note = note
                continue
            else:
                beats.append(cur_beat)
                cur_beat = 0
                continue

        if note == current_note:
            cur_beat += beat_dict[current_note]
        elif note in beat_dict:
            beats.append(cur_beat)
            cur_beat = beat_dict[note]
            current_note = note
        else:
            beats.append(cur_beat)
            cur_beat = 0
            current_note = None

    if current_note is not None:
        beats.append(cur_beat)
    return beats