from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_level in map(len, s.split()):
        result.append(bracket_level)
    return result