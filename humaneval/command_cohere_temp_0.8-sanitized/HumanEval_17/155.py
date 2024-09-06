import re
from typing import List
def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern in music string
    pattern = re.compile(r'o|o|.|.')

    # List to store beats for each note
    notes_beats = []

    # Using itertools.chain to flatten 2D list
    notes = list(re.findall(pattern, music_string))
    beats = ['four', 'two', 'one']
    result = list(itertools.chain.from_iterable(zip(notes, beats)))
    return result