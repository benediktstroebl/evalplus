def parse_music(music_string: str) -> List[int]:
    """Input to this function is a string representing musical notes in a special ASCII format.
    Your task is to parse this string and return a list of integers corresponding to how many beats each
    note lasts.

    Here is a legend:
    'o' - whole note, lasts four beats
    'o|' - half note, lasts two beats
    '.|' - quater note, lasts one beat

    """
    converter = str.maketrans(' ', '', patterned_notes)
    beat_counts = list(music_string.translate(converter).split(' ')) 
    return [4 if beat_count == 'o' else  2 if beat_count == 'o|' else 1 for beat_count in beat_counts]