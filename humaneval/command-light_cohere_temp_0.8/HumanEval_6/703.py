```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    # Use a stack to parse nested parentheses
    stack = []
    in_brace = False
    opening_brack = []

    for char in parent_string:
        if char == '(':
            stack.append(1)  # Add a new item to the stack
        in_brace = True  # Mark the start of a new group

        if char == ')':
            if not in_brace:
                stack.pop()  # Remove a stack
            in_brace = False  # Mark the end of a group
            opening_brack.append(1)  # Add the character to the opening bracket group

        if char == '(' and in_brace:
            stack.append(2)  # Add a new item to the stack

        if char == ')':
            if stack:
                stack.pop()  # Remove stack
                if stack:
                    stack.pop()  # Add stack to the opening bracket group
                    if len(stack) == 0:
                        stack.pop()  # Clear the idea of empty stack in opening bracket group. 

    output the depth of the nesting of parentheses
```