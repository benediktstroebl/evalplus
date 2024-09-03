from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_depth in map(len, s.split()):
        result.append(max(bracket_depth, result[-1] or 0))
    return result