import re
def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern of one of the four available notes.
    NOTE_PATTERN = re.compile(r'(?:o|o|.|.|o)')

    # Calculating length of the list with unique notes.
    note_count = len(NOTE_PATTERN.findall(music_string))

    # Calculating beats by counting the number of times each note appears.
    beat_count = {note: len(NOTE_PATTERN.findall(note, music_string)) for note in NOTE_PATTERN.findall(music_string)}

    return [beat_count[note] * val for note, val in NOTE_LENGTH.items() if note in beat_count]
NOTE_LENGTH = {'o': 4, 'o|': 2, '.|': 1}