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
                current_group = stack.pop() + current_group

    # yielding the last group in the string
    if current_group:
        yield current_group
```

The code leverages a stack to properly manage nested parentheses. It pushes each opened parenthesis onto the stack and pops the appropriate opened parenthesis when a closing parenthesis is encountered. This ensures that groups of parentheses are correctly separated and nested within each other.

Moreover, the code ignores any spaces in the input string by simply ignoring any ' ' characters it encounters. This is specified in the ignore clause of the function. 

The overall time complexity of the code is O(n), where n is the number of characters in the input string. This is due to the single pass required through the string to correctly separate the parentheses into groups.