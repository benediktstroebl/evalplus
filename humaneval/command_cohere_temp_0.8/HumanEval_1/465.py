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
            elif stack[-1] == "":
                stack.pop()
            else:
                current_group = stack.pop()
        else:
            current_group += char

    # yield any remaining groups in the stack
    while stack:
        yield stack.pop()
```

This script uses a stack to keep track of open parentheses `(` and uses a separate string to build the currently closed group. When it encounters a closing parenthesis `)`, it checks whether the last element in the stack is empty. If so, the group is unbalanced and we yield the current string as a group without closing it. Otherwise, we close the group and pop the corresponding opening parenthesis from the stack and append it to the current group before yielding it. Finally, if there are any remaining groups on the stack, they are yielded as well. 

The `ignore_spaces` parameter is not included in the function signature, as the spaces should not be ignored in this iteration of the problem statement. Feel free to modify the function to achieve the desired outcome of ignoring spaces.