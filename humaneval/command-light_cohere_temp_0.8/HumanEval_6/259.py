```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    output = []
    for char in parent_string:
        if char == '(': stack.append(1)
        else:
            if not stack or char == ')':
                stack.append(0)
            else:
                stack.append(stack.pop())
            result = stack
                output.return to be list of nested parentheses found in the string.
```