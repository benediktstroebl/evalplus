from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for parentheses in s.split():
        counter = 0
        nested = 0
        for char in parentheses:
            if char == '(':
                counter += 1
            elif char == ')':
                counter -= 1
                nested = max(nested, counter)
        result.append(nested)
    return result