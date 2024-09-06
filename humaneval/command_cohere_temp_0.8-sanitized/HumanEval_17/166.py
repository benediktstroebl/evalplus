import re
from typing import List
def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern in music string
    pattern = re.compile(r'o|' +
                          r'(.)|' +  # any single character except 'o' and '|'
                          r'\|(?=o|' +
                          r'(.)|' +  # any single character except 'o' and '|'
                          r'\|)')     # Ensure there is a | after the previous char to match a half note

    beat_counts = [0, 4, 2, 1]       # beat counts for respective note lengths

    return [beat_counts[pattern.match(char).span()[1] + 1]
            for char in music_string
            if char in 'o.|o|.||'
            and pattern.match(char)]