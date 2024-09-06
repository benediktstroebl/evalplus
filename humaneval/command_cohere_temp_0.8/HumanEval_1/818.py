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
                return ['Invalid input! No opening parentheses found to match this closing parenthesis.']
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    if stack:
        return ['There are unclosed parentheses groups.']
    else:
        result.append(''.join(current_group))
        return result
```
The algorithm uses a stack to keep track of opening parentheses and creates a corresponding list of strings representing each group of parentheses. It iterates through the input string, pushing each open parenthesis onto the stack and creating a new group when it encounters a closing parenthesis. The code checks for proper balancing and returns a list of separated groups, or an error message if there are unbalanced parentheses.