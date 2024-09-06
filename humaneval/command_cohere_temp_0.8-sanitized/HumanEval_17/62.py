import re
from typing import List
def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern in music string
    pattern = re.compile(r'o|' + re.escape('|') + r'(\.|o)*')
    # Returning a list with a sum operation to calculate note length
    return [sum(int(x) for x in note.group(0) if x != '|') for note in pattern.finditer(music_string)]