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
                result.append('')
            elif not stack[-1]:
                result.append('')
            else:
                stack.pop()
                current_group = stack.pop()
                result.append(''.join(current_group))
        else:
            current_group.append(char)
    
    # Handle pending groups
    while stack:
        current_group = stack.pop()
        result.append(''.join(current_group))
    
    return result
```

The algorithm uses a stack to keep track of open parentheses `(` and creates a corresponding list `current_group` to store the closed parentheses `)` and the characters between them. When it encounters a closing parenthesis, it checks if the current group is empty. If so, it appends an empty string to the result, assuming this closing parenthesis closes the outermost group. Otherwise, it pops the topmost entry of the stack (which represents a closed parenthesis and the characters between them) and appends it to the `result` list. The final result is a list where each item is a separate group of parentheses.