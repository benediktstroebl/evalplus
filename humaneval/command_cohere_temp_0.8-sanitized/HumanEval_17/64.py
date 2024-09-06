import re
def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern of one of the four notes
    note_pattern = re.compile(r'(?<!\d)(?=o)|(?<!(?=o))(?=.\.|o|o|)')

    # Calculating length of notes from given `music_string`
    beats = [len(note_pattern.findall(line)) for line in music_string.split('\n')]
    return beats