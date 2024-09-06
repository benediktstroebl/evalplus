```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """ Parse a string containing nested parentheses.
    Returns a[Order of nesting: ()(), ((())), ((()())) ]
    """
    stack: List[int] = []
    opening_brack = 0
    closing_brack = 0
    nesting_level = 0

    for char in s:
        if char == '(':
            opening_brack += 1
        stack.append(opening_brack)
        nesting_level += 1
        if char == ')':
            closing_brack += 1
            stack.append(closing_brack)
        if char == ' ':
            nesting_level -= 1
            if nesting_level == 0:
                opening_brack = 0
                closing_brack = 0
                stack.pop()

    out: List[int] = stack
    return out
```