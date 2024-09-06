def parse_music(music_string: Pattern) -> List[int]:
    MOD = 4  # Whole note lasts four beats
    NOTES = {'o': 4, 'o|': 2, '.|': 1}

    beats = []
    curr_note = None
    beat = 0

    for c in music_string:
        if c in NOTES:
            if curr_note is not None:
                beat += 1
                beats.append(beat)
                beat = 0
            curr_note = c
        else:
            beat += 1 if curr_note == 'o' else 2
            beats.append(beat)

    return beats