def parse_music(music_string: Pattern) -> List[Beats]:
    NOTES = {'o': 4, 'o|': 2, '.': 1}
    return [NOTES.get(note, 0) for note in music_string]