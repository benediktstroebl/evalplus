Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings that represent separate groups of parentheses. The script also includes a test case to demonstrate the function:
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
                return []  # Unbalanced group, returning empty list as an indicator
            current_group = stack.pop()
        else:
            current_group.append(char)

    # Handle the last group
    if stack:
        result.extend(stack)
    else:
        result.append(''.join(current_group))

    return result

# Test case
assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
```
This script uses a stack to keep track of nested parentheses and iterates through the input string. When an open parenthesis is encountered, it pushes the current group (if any) to the stack and starts a new group. When a close parenthesis is encountered, it checks if the stack is empty, indicating an unbalanced group, and if not, it pops the last group from the stack and appends it to the result. The resulting list contains separate groups of parentheses without any nesting.