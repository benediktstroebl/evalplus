import re
def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern of one of the four notes
    note_pattern = r'(?P<whole_note>o)|(?P<half_note>o\|)|(?P<quarter_note>.\|)'

    # Using recursive regex to extract all notes from the string
    beats = []
    for match in re.finditer(note_pattern, music_string):
        note = match.group()
        if note == 'o':
            beats.append(4)
        elif note == 'o|':
            beats.append(2)
        elif note == '.|':
            beats.append(1)
        else:
            beats.append(0) # Unknown note, default to 0 beats
    return beats