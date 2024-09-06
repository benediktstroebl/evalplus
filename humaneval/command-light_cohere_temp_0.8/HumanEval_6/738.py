```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    stack = []
    out = []
    for char in s:
        if char == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                out.append(0)
            else:
                stack.append(stack.pop()
               while len(stack) == 0)
                stack = []
    return out


# Test case 1
# Test case 1: Input is a string represented multiple groups for nested parentheses separated by spaces
# Output should be [2, 3, 1, 3]
parse_nested_parens('(()()) ((())) () ((())()())')')
```