from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for partition in s.split():
        level = 0
        balance = 0
        for char in partition:
            if char == '(':
                level += 1
                balance += 1
            elif char == ')':
                level += 1
                balance -= 1
        result.append(balance)
    return result