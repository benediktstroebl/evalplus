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
                result.append(''.join(current_group))
            else:
                temp = stack.pop()
                current_group.extend(temp)
            current_group.append(char)
        else:
            current_group.append(char)
            
    if not stack:
        result.append(''.join(current_group))
    else:
        while stack:
            temp = stack.pop()
            current_group.extend(temp)
        result.append(''.join(current_group))
            
    return result
```

The algorithm uses a stack to keep track of open parentheses and a list to assemble the strings for each group, ignoring spaces. It iterates through the input string, pushing onto the stack whenever it encounters an open parenthesis `(`. It empties the current group and appends it to the result whenever it encounters a closing parenthesis `)`. The current group is extended back onto the stack whenever a closing parenthesis is encountered, allowing the program to correctly assemble nested groups. The final result is a list of separated string groups.