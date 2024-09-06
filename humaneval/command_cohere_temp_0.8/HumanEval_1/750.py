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
                print(f"Invalid input: {char} is not inside any group.")
            else:
                popped = stack.pop()
                current_group.extend(popped)
        else:
            current_group.append(char)
    
    stack.extend(current_group)
    result.extend(stack)
    
    return result
```

This Python script takes a `paren_string` as input, which contains multiple groups of nested parentheses. It aims to separate these groups into individual strings and return them in a list.

To achieve this, it uses a stack (`stack` variable) to keep track of the nested parentheses. It iterates through each character in the input string:
- When it encounters an open parenthesis `'('` it pushes the current group `current_group` onto the stack and starts a new group.
- When it encounters a close parenthesis `')'`, it checks if the stack is empty. If it's not, then the top of the stack is popped and added to the current group. This process continues until the opening parentheses for that group are matched with closing parentheses.
- For any other character (either a parentheses or a symbol), it's added to the current group.

After processing all characters, any remaining items in the stack are added to the current group and hence to the result list. This ensures that all groups are properly closed, and not nested within each other. The resulting list of strings is then returned.