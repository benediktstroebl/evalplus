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
            if not stack:
                result.append(')')
            else:
                stack.pop()
                current_group.append(')')
        else:
            current_group.append(char)
    
    result.extend(current_group)
    return result

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack to keep track of nested parentheses and creates a corresponding list of strings representing the separate groups of parentheses. Oftentimes, stack data structures are used for this type of problem. The code then walks through the given string character by character, utilizing the stack to determine when a group of parentheses is closed. When a closing parenthesis is encountered, the stack is checked to see if it is empty, evaluating whether the parenthesis is the last one in its group or nested within another group. Hence, this algorithm appropriately separates groups of parentheses.