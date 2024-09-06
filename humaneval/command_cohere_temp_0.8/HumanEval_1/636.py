```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = []
    result = []
    
    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = []
        elif char == ')':
            if not stack:
                return []  # unbalanced group, returning empty list as result
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack
```
The algorithm uses a stack to keep track of opening parentheses until it encounters a closing parenthesis. Then it checks if the stack is empty to validate if the group is balanced. If so, it adds the current group to the results and repeats the process until finishing the string. It's important to note that the function returns a list of separate strings, considering that a list is mutable and allows easier grouping. The final list is returned after the stack has been popped and the content of the last group has been added.