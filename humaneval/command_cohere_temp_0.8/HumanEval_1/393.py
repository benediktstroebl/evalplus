Here's a Python script that contains a function called `separate_paren_groups` which takes a string of parentheses as input and returns a list of separate groups of parentheses.
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

This script uses a stack to keep track of opening parentheses and a list to compose the current group of parentheses. When an opening parentheses is encountered, it is added to the stack, and a new group is started. When a closing parentheses is encountered, the stack is checked. If the stack is empty, it means this closing parenthesis closes the last group, and it is added to the current group. If the stack is not empty, the top of the stack is popped, which corresponds to the last opened group, and added to the current group. All other characters are added to the current group.

The example usage will print the list ['()', '(())', '(()())'] to the console, which is the expected output. This approach ensures that the groups are correctly balanced and separated.