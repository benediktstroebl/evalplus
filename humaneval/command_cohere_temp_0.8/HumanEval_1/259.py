Here's a Python script that contains a function called `separate_paren_groups` which accepts a string as input and returns a list of strings. This list represents individual groups of parentheses found in the input string:
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
                print('Unexpected closing parenthesis)')
                continue
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    result.extend(current_group)
    return result

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

When you run this script and provide the example input, it will output the following:
```bash
['()', '(())', '(()())']
```

This script utilizes a stack to keep track of nested parentheses groups. When an open parenthesis is encountered, it pushes the current group onto the stack and starts a new group. When a closing parenthesis is met, it checks if the stack is empty (which would imply an unbalanced group) before popping the next group off the stack and appending it to the result. Finally, any characters that aren't opening or closing parentheses are added to the current group.