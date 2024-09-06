from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        nesting = 0
        balance = 0
        for char in chunk:
            if char == '(':
                balance += 1
                nesting = max(nesting, balance)
            elif char == ')':
                balance -= 1
        result.append(nesting)
    return result