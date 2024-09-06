import re
from typing import List
def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern in music string
    pattern = re.compile(r'o|\|.?|')

    # Creating an empty list to save beats for each note
    result = []

    # Using itertools.chain to save each matched object and adding 0 beat notes to the list
    result = list(re.findall(pattern, music_string)) + [0] * len(music_string)

    return result