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
            current_group += char
            if not stack:
                yield current_group
            elif stack[-1] == current_group:
                stack.pop()
                current_group = stack.pop() if stack else ""
            else:
                current_group = ""
        else:
            current_group += char

    # Yield any remaining groups
    while stack:
        yield stack.pop()
```

This Python script uses a stack to keep track of nested parentheses groups. When the input string is fed into the function, it iterates through each character. When an open parenthesis `(` is encountered, the current group is added to the stack, and a new empty group is created. When a closing parenthesis `)` is encountered, the function checks whether it matches the last group on the stack. If it does, the group is popped from the stack and added to the current group, closing the group. If it doesn't, the current group is emptied and pushed onto the stack to be handled later. The function handles situations where closing parentheses are not matched with their correct opening parentheses by saving them in a stack and revisiting them once their matching opening parentheses arrive.

The function finally returns a list of strings containing separate parentheses groups after processing the input string.