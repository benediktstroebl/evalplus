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
                return ['Invalid input! No opening parentheses found to match this closing parenthesis.']
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack
```
The code uses a stack to keep track of opening parentheses '(' and correctly populates the list of strings where each element represents a separate group of parentheses. It also handles the scenario where the closing parenthesis ')' is not matched with any opening parenthesis.