import re
from typing import List
def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern in music string
    pattern = re.compile(r'o|o|.|_|', re.IGNORECASE)

    # Calculating length of list according to how many beats each note lasts
    beats = ['4', '2', '1']

    return [beats[match.group(0) in 'o|'] * int(match.group()) for match in pattern.finditer(music_string)]