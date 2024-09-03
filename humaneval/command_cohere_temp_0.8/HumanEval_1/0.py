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
                return []  # unbalanced group, returning empty list as convention
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack
```
The provided Python script completes the task of separating nested parentheses into separate groups, achieving this through a stack data structure. Initially, the stack is empty, and a buffer named `current_group` is used to store the current group of parentheses. As the script iterates through each character of the input `paren_string`, it checks if the character is an opening parenthesis `(`. If so, the current group is pushed onto the stack and a new, empty group is initiated. Conversely, if the character is a closing parenthesis `)`, the script verifies if the stack is empty. If it is, an empty list is returned to indicate an unbalanced group. Otherwise, the top element is popped from the stack, restoring the previous group to continue processing. Any non-parentheses characters are directly appended to the current group.

Once all characters have been processed, the current group is pushed onto the stack, and the function returns the contents of the stack, resulting in a list of separate parentheses groups. This approach ensures that unbalanced or nested groups are correctly identified and handled according to the problem constraints.