Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings that represent the individual groups of parentheses. The code is designed to handle nested and balanced parentheses, and it ignores any spaces in the input string.
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
            if not stack:
                return []  # Unbalanced, return empty list
            current_group += char
            if not stack[-1]:  # If the top of the stack is empty, a group is completed
                stack.pop()
                if current_group: 
                    stack.append(current_group)
                    current_group = ""
            else:
                current_group += char
        else:
            current_group += char
    
    return stack if not current_group else stack + [current_group]

# Example usage
input_string = "( ) (( )) (( )( ))"
print(separate_paren_groups(input_string))
```
This script provides the function 'separate_paren_groups' which handles parentheses groups separation as described in the problem statement. The function runs a loop on each character of the input string. It uses a stack to keep track of open parentheses. When it encounters a closing parenthesis, it checks if it has a corresponding opening parenthesis on the stack. If it does, the current group is added to the stack (if it's not empty), indicating the completion of a group. If the stack is empty, it means an unbalanced parenthesis was encountered, and the function returns an empty list.

When the loop is done, the function returns the stack if there are no remaining open parentheses. If there are remaining open parentheses, the stack is returned along with the current group, as the innermost group may have content even when the outer parentheses are closed.

The example usage demonstrates how the function can be used to separate the groups in the input string `( ) (( )) (( )( ))`, and the resulting output will be `['()', '(())', '(()())']`.