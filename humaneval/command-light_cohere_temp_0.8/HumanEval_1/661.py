```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """Separate groups of balanced parentheses from the input string."""
    result = []
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                result.append(''.append(stack.pop())
                stack.else: pass
   
            stack is empty, add ')' to result
        else:
            raise ValueError("Unbalanced group of parentheses detected!")
    return result
```