from typing import List
def parse_music(music_string: str) -> List[int]:
    # Regular expression pattern matching table
    # Each char corresponds to a note length
    NOTE_PATTERN = 'o|^.-^|O|X|-.|'
    beat_lengths = {c:n for n,s in enumerate(NOTE_PATTERN, 1) for c in s}

    return [beat_lengths[c] for c in music_string]