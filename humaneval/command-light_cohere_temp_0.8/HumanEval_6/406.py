```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for char in s:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if not stack or stack[-1] == 1:
                result.append(len)
            stack.remove(stack)
        else:
                stack.append(0)
    elif char == ' ':
                    stack.append(0)
                continue
    return result
def test_parse_nested_parens():
    s = "(()()) ((())) () ((())()())"
    return parse_nested_parens(s) == [2, 3, 1, 3]
```