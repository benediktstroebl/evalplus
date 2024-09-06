import re
from typing import List
def parse_music(music_string: str) -> List[int]:
    # Regular expression to match a pattern in music string
    pattern = re.compile(r'o|' +
                          r'(\.|o|o|)' +
                          r'|\.|' +
                          r'o|' +
                          r'o|' +
                          r'(\.|o|o|)' +
                          r'|\.|' +
                          r'o|' +
                          r'o|' +
                          r'(\.|o|o|)')

    # Using list comprehension to extract matches and convert them to int
    return [len(list(group)) * 4 // 2 for match in pattern.findall(music_string) for group in match]