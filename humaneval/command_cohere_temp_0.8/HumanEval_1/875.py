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
                print(' mismatched closing parenthesis')
                return None
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    if stack:
        print(' unbalanced input -- missing closing parenthesis')
        return None
    
    return result if result else [None]
```

This script uses a stack to keep track of nested parentheses groups. It iterates through the input string, pushing a new group onto the stack whenever it encounters an open parenthesis. When it encounters a closing parenthesis, it checks if the stack is empty (which would indicate an unbalanced group). If not, it pops the top group off the stack and appends it to the `current_group`. Non-parenthesis characters are appended to the current group.

Finally, after processing the entire string, it checks if the stack is empty. If so, it returns the list of nested groups. If not, it prints an error message indicating a missing closing parenthesis and returns `None`. 

This approach ensures that the function correctly identifies and separates balanced parentheses groups, handling cases with and without spaces between parentheses and handling both unbalanced and nested groups.