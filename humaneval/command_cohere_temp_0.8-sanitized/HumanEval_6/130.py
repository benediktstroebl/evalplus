from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for token in s.split():
        depths = [x == '(' for x in token]
        max_depth = max(depths)
        result.append(max_depth)
    return result