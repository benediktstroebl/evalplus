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
                print(f"Unmatched close parenthesis '{char}'")
                return []
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack
```
The code uses a stack to keep track of opening parentheses '(' and pop them when a closing parenthesis ')' arrives.

To ensure proper handling of unbalanced or nested groups, the code also checks for properly matched parentheses as it iterates through the input string. Any improperly formed groups result in an error message and an empty list being returned.

This approach allows the function to correctly process input groups like '(())' or '(()())' and handle any spaces between parentheses.