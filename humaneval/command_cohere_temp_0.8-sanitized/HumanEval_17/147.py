import re
def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern of one of the four available notes.
    note_pattern = re.compile(r'(?P<whole_note>o)|(?P<half_note>o\|)|(?P<quarter_note>.\.|o\|\.)|(?P<eighth_note>.|o\|\/.)')

    # Define dictionary to translate matched groups to number of beats.
    beat_dict = {
        'whole_note': 4,
        'half_note': 2,
        'quarter_note': 1,
        'eighth_note': 1/2
    };

    # Use regex to find all occurrences of notes in the string.
    notes = list(note_pattern.finditer(music_string))

    # Initialize an empty list to store beats and iterate through matches.
    beats = []
    for match in notes:
        for beat in match.groups():
            if beat:
                beats.append(beat_dict[beat[0]])

    return beats