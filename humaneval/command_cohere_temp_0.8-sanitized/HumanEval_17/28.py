def parse_music(music_string: str) -> List[int]:
    result = []
    notes = []

    current_note = None

    for char in music_string:
        if char in 'o|.|':
            if current_note is not None:
                notes.append(current_note)
            current_note = Patterns[char]
        else:
            if current_note is not None:
                notes.append(current_note)
            current_note = None

    if current_note is not None:
        notes.append(current_note)

    return notes