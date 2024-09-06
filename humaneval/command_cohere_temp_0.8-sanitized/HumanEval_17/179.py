def parse_music(music_string: Pattern) -> List[int]:
    whole_note = 4
    half_note = 2
    quarter_note = 1

    beats = []

    for note in music_string:
        if note == 'o':
            beats.append(whole_note)
        elif note == 'o|':
            beats.append(half_note)
        elif note == '.':
            beats.append(quarter_note)
        else:
            beats.append(0)

    return beats