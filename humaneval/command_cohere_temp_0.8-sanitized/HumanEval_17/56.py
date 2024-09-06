from typing import List
PATTERN = '<WholeNote>([wW])|<HalfNote>([hH])|<QuarterNote>([qQ]|.)'
def parse_music(music_string: str) -> List[int]:
    return parse_notes(re.findall(PATTERN, music_string))
def parse_notes(note_strings: List[str]) -> List[int]:
    return [parse_note(note) for note in note_strings]
def parse_note(note: str) -> int:
    note = note.strip('wWohHqQ.')
    if note.isalpha():
        return {'w': 4, 'W': 4, 'h': 2, 'H': 2, 'q': 1, 'Q': 1}.get(note, 0)
    else:
        return 0