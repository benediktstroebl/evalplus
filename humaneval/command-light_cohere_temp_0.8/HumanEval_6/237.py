```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    """
    This function takes a string with multiple groups of parentheses separated by spaces as input and returns the deepest level of nesting of parentheses in the input string.
    """
    groups: [(')', '(', ')', '(', '()'), ('()', '()')]
    deepest_level = 0
    stack = []

    for char in parentheses_string:
        if char == '(':
            stack.append(deeper)
        stack.append(char)
        continue

        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.push(deeper)
                stack.push(char)
                continue

    if stack:
        deepest_level = max(stack) + 1
        return [deepest_level]

    return []
```