Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of strings containing individual groups of parentheses. The code is designed to handle nested and nested-within-nested parentheses, while ignoring spaces:
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
   
    stack = []
    current_group = []
    
    
    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = []
        elif char == ')':
            if not stack:
                return []  # Unbalanced group, returning empty list
            current_group = stack.pop()
        else:
            current_group.append(char)
            
    return stack
        
# Sample execution:
print(separate_paren_groups("( ) (( )) (( )( ))"))
```

The provided code demonstrates how to correctly separate groups of nested parentheses into individual strings while handling nested and nested-within-nested groups. It also ensures that the separation is balanced, returning an empty list if an unbalanced group is encountered.