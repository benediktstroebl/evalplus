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

The code uses a stack to keep track of nested parentheses groups. It utilizes the following logic:
1. If the current character is `(` it means a new group is starting, so the current group is added to the stack and a new, empty group is initiated.
2. If the current character is `)` the following logic happens:
     - If the stack is empty, it means we've reached the end of a group, hence we add `)` to the result as a signal to properly close the group in the output.
     - If the stack is not empty, it means we've encountered a nested group. We pop the top element of the stack, which is the most recently added group, and add its content to the current group. After that, we check the stack size again, as the current group might be a sub-group of the newly popped group.
     - If the current group is not nested, it means it is an outer-most group, and we simply add it to the result. 
3. If the current character is anything but `(` and `)`, it is added to the current group. 

Once all characters have been processed, the current group is added to the result, and the function returns the list of strings that represent the balanced groups of parentheses.