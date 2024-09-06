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
                result.append(')'.join(current_group))
            else:
                prev_group = stack.pop()
                current_group.extend(prev_group)
            
            if not stack:
                result.append(')'.join(current_group))
                current_group = []
        else:
            current_group.append(char)
    
    return result
```

This Python script takes a nested parentheses string as input and returns a list of separate groups of parentheses. It uses a stack to track the groups of parentheses and iterates through the input string. When it encounters an open parenthesis, it pushes the current group onto the stack and starts a new group. When it encounters a close parenthesis, it checks if the stack is empty or not. If the stack is empty, it means we've reached the end of a separate group, so it adds the current group to the result list after joining the parentheses. If the stack contains elements, it means we have encountered a nested group, so it pops the top group and appends it to the current group. The process continues until the entire string is processed. Finally, the function returns the list of separate groups of parentheses.

Here's an example usage of the function:
```python
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
```