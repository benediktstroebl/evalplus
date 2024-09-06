import re
from typing import List
def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern in music string
    pattern = re.compile(r'o|o|_|_|', re.IGNORECASE)

    # Returning a list of lengths of all matches in the string
    return [len(match) for match in pattern.findall(music_string)]