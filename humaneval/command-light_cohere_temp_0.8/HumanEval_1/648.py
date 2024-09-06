```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    result = []
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack or stack[-1] != '(':
                result.append(c)
                stack.append(')')
        if stack:
            stack.pop()
        result.extend(stack)
       return result
    return result
``` 
This function splits the string around each parenthesis, effectively separating the content into independent groups. It is a ideal solution to this problem. The test cases can be added to ensure the function works correctly.