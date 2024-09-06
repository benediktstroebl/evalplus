def parse_music(music_string: str) -> List[int]:
    result = []
    beat = 0
    for note in music_string:
        if note in Patterns:
            beat += Patterns[note]
        else:
            beat //= 2 
        result.append(beat)
    return result