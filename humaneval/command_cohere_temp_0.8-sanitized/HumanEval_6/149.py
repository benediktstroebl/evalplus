from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for token in s.split():
        balance = 0
        i = 0
        for char in token:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            i += 1
        result.append(balance)
    return result