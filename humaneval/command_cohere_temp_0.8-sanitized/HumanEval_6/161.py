from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_bracs = segment.count('(')
        close_bracs = segment.count(')')
        result.append(open_bracs - close_bracs)
    return result