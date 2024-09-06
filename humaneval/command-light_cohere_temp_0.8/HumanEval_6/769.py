```python
from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    result = []

    for char in parentheses_string:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if not stack or stack[-1] == 1:
                result.append(len)
                stack.append(0)
            elif len(stack) > 1:
                result.append(stack.pop())
               stack[-1]
        stack.append(1)
    return result
    ```