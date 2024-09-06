```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    out = []
    for c in s:
        if c == '(': stack.append(len)
        elif c == ')':
            if not stack or stack[-1] != '()':
                out.append(len)
                stack.append(None)
        elif c == '()':
                stack.pop()
    added one for each time, but only added one.
    return out
out
``` 
This script provides a solution to the problem of nested parentheses. It uses a typing module to define a parse_nested_parens function that takes a string as input and returns a list of integers representing the deepest level of nesting for each group of parentheses.