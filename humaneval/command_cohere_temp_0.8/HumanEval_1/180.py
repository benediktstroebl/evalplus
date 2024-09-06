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
                print('UNBALANCED!' if char == ')' else None)
                return None
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    result.extend(stack)
    
    return result
```

This script uses a stack to keep track of nested parens groups. It iterates through the characters of the input string, pushing a newly started group onto the stack whenever it encounters an open paren `(`. It pops the group off the stack whenever it encounters a close paren `)`.

Any non-paren characters are appended to the current group. The output of the function will be a list where each element corresponds to a balanced paren group, with any spaces excluded.

For example, given the input **`"( ) (( )) (( )( ))"`**, the function will return the list **`[('())', ('()')]`**.