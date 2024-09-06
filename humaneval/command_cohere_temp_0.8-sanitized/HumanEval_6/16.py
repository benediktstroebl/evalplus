from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_brace = segment.count('(')
        close_brace = segment.count(')')
        result.append(open_brace - close_brace)
    return result