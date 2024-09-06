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
                print(f"Unmatched ) found '{char}'")
                return []
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack
```

This code defines a function `separate_paren_groups` that takes in a string of parentheses and splits them into separate groups based on their nesting levels. It uses a stack to keep track of open parentheses until they are closed, and accordingly, it pops the stack to close the appropriate parentheses. The inner list `current_group` keeps track of the characters within a particular group, which is then added to the result list when the group is closed. The provided example and its result are also included, alongside a test suite with related tests.