from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_par = segment.count('(')
        close_par = segment.count(')')
        result.append(open_par - close_par)
    return result