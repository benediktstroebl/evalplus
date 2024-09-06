import re
from typing import List
def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern in music string
    pattern = re.compile(r'o|' + re.escape('|') + '|' + re.escape('.') + '|' + ' '.replace('.', r'|'))
    # Using regex to find all whole, half, and quarter notes in the string
    beats = pattern.findall(music_string)
    # Transforming matches to integers
    return [4 if beat == 'o' else 2 if beat == '|' else 1 for beat in beats]