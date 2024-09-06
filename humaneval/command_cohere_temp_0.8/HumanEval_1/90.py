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
                yield current_group
        else:
            current_group += char

    # yield any remaining groups
    while stack:
        yield stack.pop()
```

This script uses a stack to keep track of open parentheses and creates a corresponding list of strings. Additionally, it utilizes Python's typing module for added clarity and readability. The function iterates through each character in the provided string, determining whether it is an open or closed parenthesis. When an open parenthesis is encountered, it pushes the current group onto the stack and starts a new group. Upon encountering a closed parenthesis, it checks whether the current group is fully balanced within the stack and yields it if it is. Alternatively, if the stack is empty, the closed parenthesis corresponds to the end of a group, and it is added to the current group. The function ultimately returns a list of all the balanced groups, irrespective of nested relationships.