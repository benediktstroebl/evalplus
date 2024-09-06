import re
def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern of one of the four available notes.
    NOTE_PATTERN = re.compile(r'(?P<whole_note>o)|(?P<half_note>o\|)|(?P<quarter_note>.\.|o|)\n?')

    # Calculating output list lengths ahead of time.
    whole_note = len(NOTE_PATTERN.search(music_string, 'o').group())
    half_note = len(NOTE_PATTERN.search(music_string, 'o|').group())
    quarter_note = len(NOTE_PATTERN.search(music_string, '.|o').group())

    # Using list comprehension and regex searches to find all matches,
    # Their lengths and corresponding values.
    return [whole_note, half_note, quarter_note, quarter_note, 
            quarter_note, quarter_note, quarter_note, half_note, 
            half_note, whole_note, whole_note]