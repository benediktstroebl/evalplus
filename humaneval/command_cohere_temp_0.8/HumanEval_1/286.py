Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separate groups of parentheses.
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
                print("Unmatched ')' found!")
                continue
            current_group.append(char)
            if not stack[-1]:
                result.append(')'.join(current_group))
                stack.pop()
                current_group = stack.pop()
            else:
                current_group = stack.pop()
        else:
            current_group.append(char)
            
    return result
```
The function uses a stack to keep track of open parentheses and navigates through the given string to separate groups of parentheses while handling nested and unbalanced scenarios. It then returns the list of separated groups.