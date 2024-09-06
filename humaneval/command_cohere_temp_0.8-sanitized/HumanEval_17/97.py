from typing import List
def parse_music(music_string: str) -> List[int]:
    # Regular expression pattern matching
    # Whole note: 'o', half note: 'o|', quater note: '.'
    beat_pattern = r'o+|o\||\.\|'

    def parse_beat(match) -> int:
        return {'o': 4, 'o|': 2, '.|': 1}.get(match.group(), 1)

    # Using annotated syntax for verbose debugging
    # See https://regex.swered.io/physics/musical-notes-keyboard/
    beats = [
        int(match.groups()[0]) * parse_beat(match)
        for match in re.finditer(beat_pattern, music_string)
    ]
    return beats