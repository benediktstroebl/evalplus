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
                return []
            current_group.append(char)
            if not stack[-1]:
                result.append(''.join(current_group))
                stack.pop()
            else:
                current_group = stack.pop()
        else:
            current_group.append(char)
            
    return result
```
The code leverages a stack to properly isolate and handle nested parentheses. It also uses a list (current_group) to accumulate characters forming a group. When a closing parenthesis ')' is encountered, the code checks if the top of the stack is an empty list. If true, there are unbalanced parentheses, hence we return an empty list. If false, the code checks if the last group in the stack is empty. If true, the current group is properly closed, and it is added to the results list and popped from the stack. If false, the current group is not closed, hence the stack pops and saves the last group and appends the current group to it. This ensures that all properly closed groups are collected in the result list.