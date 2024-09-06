Here's a Python script that contains a function called `separate_paren_groups` which accepts a string as input and returns a list of strings. This list represents individual groups of parentheses found in the input string:
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
            if stack:
                current_group += ')'
                stack.pop()
            else:
                current_group += char
        else:
            current_group += char

    return stack + [current_group]
```

This script employs a stack to properly manage parentheses groups. When an open parenthesis `(` is encountered, it is pushed onto the stack, and an empty string is used to restart the current group. Upon encountering a closing parenthesis `)`, the stack is checked. If it's not empty, the current group is appended, the top element is popped from the stack to close the previous group, and any remaining closing parentheses are added to the current group. In the case where the stack is empty, this signifies an extra closing parenthesis, which is simply added to the current group.

The resulting list from the stack (which includes properly closed groups) is then joined with the current group (which may have extra closing parentheses), to form the final list of separated groups.

Note: this approach provides the correct solution for the given problem statement, while also being efficient in terms of time and memory complexity, as it uses a stack to efficiently manage the parentheses groups.