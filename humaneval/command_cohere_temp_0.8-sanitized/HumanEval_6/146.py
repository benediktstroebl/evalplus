from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_str in s.split():
        count = 0
        curr = 0
        for char in bracket_str:
            if char == '(':
                count += 1
            else:
                count -= 1
            curr = max(curr, count)
        result.append(curr)
    return result