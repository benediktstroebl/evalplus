import re
def parse_music(music_string: str) -> List[int]:
    beat_pattern = re.compile(r'o|o|_|_|', flags=re.I)
    parsed_beats = []
    for beat_group in beat_pattern.findall(music_string):
        if len(beat_group) == 2:
            parsed_beats.append(4)
        elif len(beat_group) == 1:
            parsed_beats.append(2)
        else:
            parsed_beats.append(1)
    return parsed_beats