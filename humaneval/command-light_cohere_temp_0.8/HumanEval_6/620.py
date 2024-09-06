```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for char in s:
        if char == '(':
            stack.append(0)
        elif char == ')':
            stack.pop()
            a maximum number that could be at the end of a group, return the number in the stack.
    return output

```

This function, parse_nested_parens, takes a string of nested parentheses and returns a list of deepest-level nesting parentheses.