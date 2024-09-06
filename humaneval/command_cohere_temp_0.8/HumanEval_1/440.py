```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""
    
    for char in paren_string:
        if char == '(':
            current_group += char
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            current_group += char
            if stack:
                stack.pop()
            else:
                print(f"Unmatched right parenthesis '{char}'.")
    
    return stack
```
This code is designed to work with nested parentheses of any depth. It uses a stack to keep track of the currently opened group of parentheses. When it encounters a closing parenthesis, it checks whether the top of the stack is the corresponding opening parenthesis and therefore belongs to the same group, or if it's missing - in which case the code prints an error message. The output of the function will be a list of strings, where each string corresponds to a balanced group of parentheses.