import re
from typing import List
def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern of one of the four available notes.
    NOTE_PATTERN = re.compile(r'(?P<whole_note>o)|(?P<half_note>o\|)|(?P<quater_note>.\.|o\|\.)')

    # Slices to capture the matches in the order of whole note, half note, and quater note.
    notes_description = [(NOTE_PATTERN.match(music_string[i:i+3])) for i in range(0, len(music_string), 3)]

    return [
        sum(note.group(index).isdigit() for index, note in enumerate(notes_description)) * 
            {'whole_note': 4, 'half_note': 2, 'quater_note': 1}.get(note.group('name'), 1)
        for note in notes_description
    ]