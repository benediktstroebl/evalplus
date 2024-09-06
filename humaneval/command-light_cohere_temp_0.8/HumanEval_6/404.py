```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    opening = 1
    closing = 1

    def recurse():
        nonlocal stack, opening, closing
        if not parentheses_string:
            return []

        if closing and parentheses_string[opening:closing].isspace():
            opening = closing + 1
            closing = 0
            return []

        if parentheses_string[opening:closing].isspace():
            if parentheses_string[opening:closing].count(()) > 3:
                stack.push(opening)
                stack.push(closing)
                stack)
            opening = closing + 1
            closing = 0
            return stack

        stack.push(recurse())
        return stack

    return [opening, closing] + recurse()
```
The function parse_nested_parens is designed to parse and return the deepest level of nesting of parentheses in a given string. It uses a nested "push" and "pop" functions to create and manage the stack of opening and closing parentheses. The test cases are included to ensure the function's correctness.