from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_pair in s.split():
        count = 0
        nesting_level = 0
        for char in bracket_pair:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
            nesting_level = max(nesting_level, count)
        result.append(nesting_level)
    return result