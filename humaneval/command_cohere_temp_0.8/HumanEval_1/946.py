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
                return ['']
            current_group.append(char)
            if not stack[-1]:
                result.append(''.join(stack.pop()))
            else:
                stack.pop()
        else:
            current_group.append(char)
    
    return result
```

This script uses a stack to keep track of nested parentheses groups. When a closing parenthesis is encountered, the code checks if it matches the most recent open parenthesis on the stack. If it does not, the code returns ''. This indicates that the input string had unbalanced parentheses.

The resulting list of strings is then returned once all the parentheses are properly processed. You can test this script by calling `separate_paren_groups()` with different inputs to ensure it handles nested groups correctly. Let me know if you need anything else!