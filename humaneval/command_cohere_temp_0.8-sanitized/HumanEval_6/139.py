from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for group in s.split():
        level = 0
        stack = []
        for c in group:
            if c == '(':
                stack.append(c)
            else:
                if not stack:
                    break
                level += 1
                stack.pop()
        result.append(level)
    return result