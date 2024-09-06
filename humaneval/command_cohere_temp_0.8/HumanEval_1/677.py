Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of strings of separated parentheses group:
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
                current_group.pop()
                if not current_group:
                    result.append(')')
                else:
                    stack.pop()
        else:
            current_group.append(char)
    
    return result
```

This code uses a stack to keep track of nested parentheses groups. When a closing parenthesis is encountered, the code checks if it matches the most recent opening parenthesis, either from the current group or the stack. This ensures that all parentheses groups are properly separated and not nested within each other. The final list of strings containing the separated parentheses groups is returned.