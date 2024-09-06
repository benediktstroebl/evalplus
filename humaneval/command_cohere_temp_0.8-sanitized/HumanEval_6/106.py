from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for token in s.split():
        open_par = token.count('(')
        close_par = token.count(')')
        result.append(open_par - close_par)
    return result