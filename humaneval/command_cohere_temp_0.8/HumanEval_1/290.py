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
                return ['Unbalanced brackets in: '+paren_string]
            current_group = stack.pop()
        else:
            current_group.append(char)
            
    if stack:
        return ['Unbalanced brackets in: '+paren_string]
    else:
        result.append(''.join(current_group))
        return result
```

The script uses a stack to keep track of opening brackets and collects the corresponding closing brackets. It also utilizes a separate list to store the currently collected tokens when brackets are balanced. When the entire string is traversed, the stack is checked to ensure it is empty, confirming that all brackets are balanced. The final result is the list of separated group strings.