from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for token in s.split():
        stack = []
        level = 0
        for c in token:
            if c == '(':
                stack.append(c)
                level += 1
            else:
                stack.pop()
                level -= 1
        result.append(level)
    return result