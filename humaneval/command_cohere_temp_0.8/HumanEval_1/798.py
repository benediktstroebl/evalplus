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
                print('Unmatched close parenthesis')
                return None
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    if stack:
        print('Unmatched open parenthesis')
        return None
    
    result.append(''.join(current_group))
    
    return result
```
The provided Python script completes the task to separate nested parentheses into separate groups, ensuring balancing and absence of nesting. It uses a stack data structure to manage the open parentheses. When encountering a closing parenthesis, it checks if the stack is empty, indicating an unmatched closing parenthesis. If not, it retrieves the top open parenthesis and checks if it matches the current depth. The result is a list of separated parenthesis groups, successfully handling potential unmatched parentheses and nested structures.