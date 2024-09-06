```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    Parses a string of nested parentheses into a list of the deepest level of nesting.
    >>> test_parse_nested_parens('(()()) ((())) () ((()))()')
    [(2, 3, 1, 3)]
    >>> test_parse_nested_parens('()()()()()()')
    []
    """
    stack = []
    in_string = False
    for char in s:
        if char == '(':
            if not in_string:
                stack.append(level=len)
                in_string = True
        elif char == ')':
            if len(stack) == 0 or stack[-1][0] != level:
                raise ValueError("Incorrect order of closing parenthesis!")
            stack.pop()
            stack[-1]
        in_string = False
    return stack
```