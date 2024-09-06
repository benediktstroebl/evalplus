def parse_music(music_string: str) -> List[int]:
    result = []
    curr_beat = 0
    for note in music_string:
        if note in Patterns:
            curr_beat += Patterns[note]
            result.append(curr_beat)
        elif note == '|':
            curr_beat = 0
    return result