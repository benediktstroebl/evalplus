```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """Separate groups of balanced parentheses from the input string"""
    result = []
    stack = []
    for char in s:
        if char == '(': stack.push(char)
        elif char == ')': 
            if not stack or stack[-1] != '(': 
                result.append(char)
                stack.pop()
       needed open parenthesis.push(')')
        if char == '(' and not stack: stack.push(char)
    else: stack.push(char)
    return result
```