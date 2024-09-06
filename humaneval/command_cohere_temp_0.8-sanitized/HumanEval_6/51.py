from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for token in s.split():
        open_parentheses = token.count('(')
        close_parentheses = token.count(')')
        result.append(open_parentheses - close_parentheses)
    return result