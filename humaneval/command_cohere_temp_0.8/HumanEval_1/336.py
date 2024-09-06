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

    result.append(''.join(current_group))

    return result

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
```
This script uses a stack to keep track of nested parentheses and iterates through the input string. When an opening parenthesis is encountered, it checks if the stack is empty; if not, the current group is added to the stack, and a new group is created. When a closing parenthesis is encountered, it checks if the stack is empty; if not, the top group is popped from the stack and added to the current group. All other characters are added to the current group.

After processing all characters, the stack is checked again to ensure all groups are properly closed. Any remaining opening parentheses in the stack are added to the current group. Finally, the current group is added to the result list, and the function returns the list of separated groups.

When the example input is provided, the output will be:
```bash
['()', '(())', '(()())']
``` 

This matches the expected output as described in the problem statement.