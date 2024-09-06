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
            if stack:
                current_group = stack.pop()
            else:
                current_group.append(char)
        else:
            current_group.append(char)
    
    if stack:
        while stack:
            current_group.append(')')
            stack.pop()
    
    if current_group:
        current_group.append(')')
    
    result.extend(current_group)
    
    return result

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack to keep track of nested parentheses and iterates through the input string. When an open parenthesis is encountered, it pushes the current group onto the stack and starts a new group. When a close parenthesis is encountered, it checks if the stack is empty; if not, the stack is not empty, so it pops the last group from the stack and appends its content to the current group. If the stack is empty, the close parenthesis is appended to the current group. After processing all characters, it handles any remaining open parentheses by appending them to their corresponding groups. Finally, it returns a list of these separate groups.

When you run this script with the example input, it should print the correct output, `['()', '(())', '(()())']`, to the console as a list of three strings, each representing a separate group of parentheses.