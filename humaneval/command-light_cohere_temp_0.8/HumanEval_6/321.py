Here's a Python script with a self-contained function that solves the problem of finding the deepest level of nesting of parentheses in a given string:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    opening_level = 0
    for c in s:
        if c == '(':
            opening_level += 1
        elif c == ')':
            if len(stack) == 0:
                opening_level -= 1
            elif stack[-1] > opening_level:
                stack.
            else:
                stack.
        else:
            stack.
    return [ depth_5 in stack
```
The function uses a stack to keep track of opening parentheses and closing parentheses. It starts with an opening level of 0 for each input character. It iterates through the opened parentheses will increase the opening level, and closed parentheses will decrease the opening level. This process continues until there are no more opening parentheses. The function returns the maximum of the opening levels.