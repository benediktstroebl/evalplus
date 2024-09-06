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
                current_group = stack.pop()
        else:
            current_group += char

    # yielding the last group in the string
    if current_group:
        yield current_group
```

The function uses a stack to keep track of nested parentheses groups and a current_group variable to store the current group being processed. It iterates through the input string and opens a new group when encountering the open parenthesis '(', it also starts a new group if the current group is empty. When encountering a close parenthesis ')', it checks whether the last group on the stack is equal to the current group and pops the stack accordingly. If the last group on the stack is not equal to the current group, it indicates that there is a nested group, it yields the current group, pops it from the stack, and starts the next group from the top of the stack. It yields any remaining groups on the stack before closing the function.