def parse_music(music_string: str) -> List[int]:
    result = []
    notes = []

    current_note = None
    i = 0

    while i < len(music_string):
        if music_string[i] in 'o|.|':
            if current_note is not None:
                notes.append(current_note)
            current_note = Patterns[music_string[i]]
            i += 1
        elif current_note is not None:
            current_note -= 1
            if current_note == 0:
                notes.append(current_note)
                current_note = None
        i += 1

    if current_note is not None:
        notes.append(current_note)

    return notes