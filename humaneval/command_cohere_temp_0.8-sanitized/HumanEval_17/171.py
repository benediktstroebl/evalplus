def parse_music(music_string: str) -> List[int]:
    result = []
    notes = []

    current_note = None
    beat = 0

    for char in music_string:
        if char in 'o|.' and current_note is None:
            current_note = char
        elif char in 'o|.' and current_note is not None:
            notes.append(beat)
            beat = beat + Patterns[current_note]
            current_note = None
        elif char == '|':
            if current_note is not None:
                notes.append(beat)
                beat = 0
                current_note = None
        elif char == '.':
            if current_note is None:
                raise ValueError("Invalid note format!")
        else:
            raise ValueError("Invalid note format!")

    if current_note is not None:
        notes.append(beat)

    return notes