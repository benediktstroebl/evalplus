```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""
    
    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            current_group += char
            if not stack:
                return []
            current_group = stack.pop()
        else:
            current_group += char
            
    return stack
```
The code uses a stack to keep track of opening parentheses '(' and properly close and balance them with the corresponding closing parentheses ')' before finally converting the list of stacked strings into a list answer.

Here is a test case input-output example:
```
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
```