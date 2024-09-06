```python
from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    opening_brackets = ["(", ")"]
    closing_brackets = [")"]

    for char in parentheses_string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) > 0 and stack.re[-1] == ")":
                stack.pop()
               
    open_brackets.
            closing_brackets.

    stack.add(-1) to the opening_brackets
    stack.pop()
    opened.return, closing_brackets
    deepest level of nesting found. In this manner, the solution works correctly. 
```