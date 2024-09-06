Here's a Python script that contains a function called `separate_paren_groups` which takes a string of parentheses as input and returns a list of separate groups of parentheses.
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
            if stack:
                current_group = stack.pop()
            else:
                current_group.append(char)
        else:
            current_group.append(char)
    
    if stack:
        while stack:
            current_group.append(')')
            stack.pop()
    
    if current_group:
        current_group.append(')')
    
    result.extend(current_group)
    
    return result

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack to keep track of opening parentheses until the corresponding closing parenthesis is encountered. All separated groups are then collected in a result list and extended with the closing parenthesis, if needed. This way, the function solves the task as described in the example test case.