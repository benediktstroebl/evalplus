```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    opening_levels = {}
    closing_levels = {}

    for level, char in enumerate(s, 1):
        if char == '(':
            stack.append(level)
            opening_levels[level] = True
        closing_levels[level] = True

    for level, char in enumerate(s[::-1], len(stack)):
        if char == ')':
            if stack:
                stack.pop()
               
            closing_levels[stack[-1]] = False
                closing_levels[level] = False
                if level == len(stack) - 1:
                    if not closing_levels[stack[-1]] and stack:
                        opening_levels[stack[-1]] = False
                    stack = []
            else:
                closing_levels[level] = False

    return [i for i, _ in enumerate(stack, 1, -1)]


# Test cases
def test_parse_nested_parens():
    test_strings = {
        "(()()) ((())) () ((())()())": [2, 3, 1, 3],
        "((()))" : [1],
        "((())) () () ((()))": [2, 3, 1, 3],
        "(((((((())))))))))": [1, 2, 3],
        "()()() () () ()()": [4, 3, 1, 3],
        "() ( )()": []
    }

    for s, expected in test_strings.parse_nested_parens(s):
        assert expected == parse_nested_parens(s), f"Failed for: {s}, expected: {expected}, actual: {parse_nested_parens(s)}"


If you have any other questions related to Python or coding, feel free to ask! I'm here to help you in exploring and learning. I can assist with many other coding problems and provide better solutions or insights!