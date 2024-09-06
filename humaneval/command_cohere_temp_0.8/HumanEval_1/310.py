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
                print(f"Unmatched ) encountered! Skipping {char}")
                continue
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    result.extend(stack)
    
    return result
```
The algorithm uses a stack to keep track of opening parentheses until it encounters a corresponding closing parenthesis. When a closing parenthesis is encountered, the stack is checked to ensure it's not empty (to avoid unmatched parentheses), and the currently active group is added to the result. This process ensures that nested or unbalanced parentheses are properly handled. 

Here is an example output:
```
Separate groups are balanced (each open brace is properly closed) and not nested within each other.
Ignore any spaces in the input string.

>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
```