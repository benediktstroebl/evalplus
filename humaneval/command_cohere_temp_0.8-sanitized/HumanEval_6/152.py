from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result, levels = [], 0
    for segment in s.split():
        if not segment:
            continue
        opening, closing = segment.count('('), segment.count(')')
        levels += opening - closing
        result.append(levels)
    return result