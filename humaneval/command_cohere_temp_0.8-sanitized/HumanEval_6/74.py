from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_parentheses = segment.count('(')
        close_parentheses = segment.count(')')
        result.append(open_parentheses - close_parentheses)
    return result