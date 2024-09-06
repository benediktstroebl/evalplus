import re
from typing import List
def parse_music(music_string: str) -> List[int]:
    # Use regex to find all whole, half and quarter notes in the string
    beat_pattern = re.findall(r'(?<!\d)(o|o|.)', music_string)
    # Use regex to convert found notes to integer values
    beat_values = [4 if n == 'o' else 2 if n == 'o|' else 1 for n in beat_pattern]
    return beat_values