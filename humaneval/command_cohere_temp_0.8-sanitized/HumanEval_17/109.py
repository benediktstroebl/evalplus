import re
from typing import List
def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern of one of the four available notes.
    NOTE_PATTERN = re.compile(r'(?P<whole_note>o)|(?P<half_note>o\|)|(?P<quarter_note>.\|)'
                              r'(?P<rest>|[^\W\d]|$)')

    # Defines a function which takes a musical string and returns a list of integers.
    beats = []
    for match in NOTE_PATTERN.finditer(music_string):
        note = match.group()
        note_beat_length = {
            'whole_note': 4,
            'half_note': 2,
            'quarter_note': 1
        }.get(match.group('note_type'))
        
        if note == '':  # It is a rest
            note_beat_length = 0
        beats.append(note_beat_length)
    return beats