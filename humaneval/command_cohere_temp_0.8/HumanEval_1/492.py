Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separate groups of parentheses.
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
                print("Unbalanced groups")
            else:
                current_group = stack.pop()
        else:
            current_group.append(char)
    
    result.extend(current_group)
    return result
```
The script uses a stack to keep track of open parentheses `(` and creates a corresponding list `current_group` to store the characters between parentheses. When it encounters a closing parenthesis `)`, it checks if the stack is empty; if so, it prints an message indicating unbalanced groups, whereas otherwise, it pops the top element of the stack and appends it to the `current_group`. The final result is a list where each item is a separate group of parentheses, and it's returned to the caller.