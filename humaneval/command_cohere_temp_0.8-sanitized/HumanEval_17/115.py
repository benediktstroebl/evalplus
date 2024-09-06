import re
from typing import List
def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern in music string
    pattern = re.compile(r'o|' + re.escape('|') + r'(\.|o)')

    # Return list where each element corresponds to length of a beat
    return [len(m.group()) for m in pattern.finditer(music_string)]