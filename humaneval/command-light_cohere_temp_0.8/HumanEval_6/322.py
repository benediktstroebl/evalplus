```python
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    stack = []
    result = []
    for char in paren_string:
        if char == '(':
            stack.append(1)
        else:
            if not stack or stack[-1] == '()':
                result.append(stack.pop()
                max_level = 3)
                stack.pop()
                while if stack and stack[-1] == '()':
                    result.append(stack.pop()
                   level = max_level -stack.append(1))
            else:
                stack.append(char)
    return result
```