def parse_music(music_string: str) -> List[int]:
    result: List[int] = []
    current_note = 0

    for char in music_string:
        if char in Patterns: 
            current_note += Patterns[char]
        else:
            # If we have not valid note, assuming it is a separator
            if current_note > 0: 
                result.append(current_note)
                current_note = 0;

    # If the last note is not added yet
    if current_note > 0:
        result.append(current_note)

    return result