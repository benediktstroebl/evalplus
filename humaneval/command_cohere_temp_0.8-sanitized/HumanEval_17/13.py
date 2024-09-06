import re
from typing import List
def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern in music string
    pattern = re.compile(r'o|o|_|_|', re.IGNORECASE)

    # Empty music string returns empty list
    if not music_string.strip():
        return []

    # Each beat group consists of a whole note o and two half notes o| or _|_
    beat_group = re.findall(pattern, music_string)
    # Transforming beat groups to beats array
    beats = [4, 2, 1] * (len(beat_group) // 3)

    # If the music string is not a multiple of a beat group long,
    # the last beat group is chopped by one
    beats[-1] = beats[-1] // 2

    return beats