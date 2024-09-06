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
                print(f"Invalid input - extra closing brace: {char}")
                return []
            current_group.pop()
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    if stack:
        print(f"Invalid input - unclosed brace")
        return []
    
    result.append("".join(current_group))
    return result
```
The algorithm uses a stack to keep track of opening parentheses until it encounters a corresponding closing 
parenthesis. At that point, it checks if the stack is empty (which would mean an extra closing brace) or if
the top of the stack matches the expected opening parentheses, restoring the balance. The result is a list 
of strings, each representing a balanced group of parentheses.