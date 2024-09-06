def parse_music(music_string: Pattern) -> List[int]:
    BEAT = {'o': 4, 'o|': 2, '.': 1}
    return [BEAT[note] for note in music_string]