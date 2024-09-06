from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        depth = 0
        balance = 0
        nesting_level = 0
        for char in segment:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
                nesting_level = max(nesting_level, balance)
            if balance < 0:
                break
        result.append(nesting_level)
    return result