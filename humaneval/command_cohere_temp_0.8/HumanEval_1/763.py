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
                result.append(')')
            else:
                temp_group = stack.pop()
                current_group.extend(temp_group)
                if not stack:
                    result.append((').extend(current_group)')
                else:
                    current_group = []
        else:
            current_group.append(char)
    
    if current_group:
        result.append(')'.join(current_group))
    
    return result
```

The algorithm utilizes a stack to keep track of nested parentheses groups. When an open parenthesis `(` is encountered, it is added to the stack, and a new group is created. Upon encountering a closing parenthesis `)`, the stack is checked. If it is empty, it signifies an unmatched closing parenthesis, hence it is added to the result as is. However, if the stack is not empty, the current group is appended to the most recent open group at the top of the stack, and the stack is popped to reduce the group count by one.

This process continues, with the current group capturing all characters between parentheses. Once the entire string is processed, any remaining groups that haven't been matched with a closing parenthesis are added to the result. These are joined with a closing parenthesis `)`.

The result is a list of strings that encapsulate each balanced group of parentheses found in the input string, excluding any spaces.