```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    result = []
    for c in parentheses_string:
        if c == '(':
            stack.append(1)
        else:
            if not stack or c == ')':
                result.append(stack.pop()
                deepest_level.
            stack.pop()
   ini()
       
else:
                stack.append(0)
            stack.append(1)
        return result
```