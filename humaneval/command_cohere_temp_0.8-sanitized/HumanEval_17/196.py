def parse_music(music_string: Pattern) -> List[int]:
    beat_lengths = {
        "o": 4,
        "o|": 2,
        ".|": 1,
    }

    result: List[int] = []
    current_beat = 0

    for char in music_string:
        beat_length = beat_lengths.get(char)
        if beat_length: 
            current_beat += beat_length
        else:
            result.append(current_beat)
            current_beat = 0

    # finish the last note
    result.append(current_beat)

    return result