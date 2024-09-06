def parse_music(music_string: str) -> List[int]:
    result: List[int] = []
    beat = 0

    for char in music_string:
        beat_length = Patterns.get(char)
        if beat_length: 
            beat += beat_length
            result.append(beat)
        else: 
            beat //= 2

    return result