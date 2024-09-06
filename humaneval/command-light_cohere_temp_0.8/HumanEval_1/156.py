```python
from typing import List
def separate_paren_groups(parenthesis: str) -> List[str]:
    result = []
    stack = []
    for char in parenthesis:
        if char == '(': stack.append(char)
        else:
            if not stack or stack[-1] == ')':
                result.append(char)
                stack.append(')')
            else:
                result.append(') ' + stack.append('(')
                stack.append(')')
   
        return result
```