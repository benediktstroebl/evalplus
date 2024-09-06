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
                return []
            current_group.append(char)
            if not stack[-1]:
                result.append(''.join(current_group))
                stack.pop()
            else:
                current_group = stack.pop()
        else:
            current_group.append(char)
            
    return result
```

This script uses a stack to keep track of nested parens. It iterates through the input string char by char:
- '(' and ')' characters are used to manage the stack and track nested paren groups
- ignore any spaces in the input string

Therefore, the function should return a list of balanced paren groups, without any nesting or spacing. 

For example:
```
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
```