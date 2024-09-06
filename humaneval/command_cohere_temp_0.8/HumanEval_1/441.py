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
                print('UNBALANCED!')
            else:
                popped_group = stack.pop()
                current_group.extend(popped_group)
        else:
            current_group.append(char)
    
    stack.extend(current_group)
    result.extend(stack)
    
    return result
```

This Python script takes a markdown line (`paren_string`) and turns it into a list (`result`) of strings. The `separate_paren_groups` function iterates through each character in the string. When it encounters an open parenthesis `(`, it pushes the current string onto a stack and starts a new empty string. Upon encountering a closing parenthesis `)`, it checks if the stack is empty. If it's not, the function pops a string from the stack, appends it to the current string, and continues iterating through characters. This process effectively separates groups of parentheses into different strings. The resulting list of strings is achieved without any nested or unbalanced parentheses.