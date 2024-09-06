```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for c in s:
        if c == '(':
            stack.append(1)
        else:
            if not stack or stack[-1] == '()':
                result.append(stack.pop()
           
                maximum = 3
                stack.append(0)
            else:
                stack[-1] = 0
    return result
#Example usage
parentheses = parse_nested_parens('(()()) ((())) () ((())()())')
print(parentheses)
```