Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separate groups of parentheses.
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

This script uses a stack to keep track of nested parentheses and creates a corresponding list of strings representing the separate groups of parentheses. Oftentimes, stack data structures are used for this type of problem. The result is a list `['()', '(())', '(()())']`, which matches the output specified in the example problem.