```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    open_parens = {}
    closing_parens = {}
    output = []
    for char in s:
        if char == ')':
            key = stack.pop()
            if key and closing_parens[key]
            output.append(closing_parens[key])
            closing_parens[key] = None
        elif char in open_parens:
            stack.append(open_parens[char])
        else:
            open_parens[char] = stack.append(char)
    stack.finally in closing, e. most a list of parentheses, we can use a stack and a dictionary to keep track of the open and closed parentheses.