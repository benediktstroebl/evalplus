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
                print('Unmatched closing parenthesis')
                return []
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    if stack:
        print('Unmatched opening parenthesis')
        return []
    
    result.extend(current_group)
    return result
```

This script uses a stack to keep track of opening parentheses '(' and properly close them with their matching counterparts ')' while disentangling the strings. It also handles the case when the input string ends with an unmatched opening parenthesis.