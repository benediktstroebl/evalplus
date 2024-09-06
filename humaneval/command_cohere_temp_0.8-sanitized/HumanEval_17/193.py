def parse_music(music_string: Pattern) -> List[int]:
    beat_lengths = {
        "o": 4,
        "o|": 2,
        ".|": 1,
    }

    return [beat_lengths[note] for note in music_string]