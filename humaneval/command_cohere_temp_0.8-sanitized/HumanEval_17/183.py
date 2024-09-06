import re
from typing import List
def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern in music string
    pattern = re.compile(r'o|' + re.escape('|') + r'(\.|o)')
    # List to store beats for each note
    beats = []
    # Iterate over each match of the pattern in music string
    for match in re.finditer(pattern, music_string):
        note = match.group(1)
        if note == 'o':
            beats.append(4)
        elif note == '.':
            beats.append(1)
        # If match has bar line '|', add 2 to the last note
        if match.group(0) == 'o|':
            beats[-1] += 2
    return beats