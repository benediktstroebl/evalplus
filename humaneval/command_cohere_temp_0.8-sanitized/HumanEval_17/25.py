import re
def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern of one of the four available notes.
    NOTE_PATTERN = re.compile(r'(?P<whole_note>o){1,2}'
                             r'(?P<half_note>o|)|'
                             r'(?P<quarter_note>.\.){1,2}')

    # Define dictionary to translate matches into integer note values.
    note_values = {'whole_note': 4, 'half_note': 2, 'quarter_note': 1}

    # Return list where each element is the length of a line from the input string.
    return [sum(note_values[match.group()] for match in NOTE_PATTERN.finditer(line))
            for line in music_string.split('\n')]