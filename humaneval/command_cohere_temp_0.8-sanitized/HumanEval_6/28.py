from typing import List
def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        level = 0
        unbalanced = 0
        stack = []
        for char in segment:
            if char == '(':
                stack.append(char)
                unbalanced += 1
            else:
                unbalanced -= 1
                if not unbalanced:
                    level += 1
                if stack and not unbalanced:
                    level += 1
                stack.pop()
        result.append(level)
    return result