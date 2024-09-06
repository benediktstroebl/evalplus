import re
from typing import List
def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern in music string
    pattern = re.compile(r'o|o|.|.')

    # List of tuples with beats and number of occurrences per beat
    notes = [(4,), (2,), (1,), ()]

    # Using map to replace matched patterns with corresponding beats
    beats = list(map(lambda x: x[0], pattern.findall(music_string)))

    # Zipping to get number of occurrences for each beat
    return list(zip(*beats))