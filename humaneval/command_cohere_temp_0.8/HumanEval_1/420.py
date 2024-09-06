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

    # yield the last group in the string
    if current_group:
        yield current_group
```

The code uses a stack to keep track of nested parentheses groups and a current_group variable to store the current group separated from the rest of the groups. It iterates through the characters of the input string, when encountering an open parenthesis, the current group is added to the stack and a new empty group is created. When encountering a closing parenthesis, the code checks whether it matches the last group in the stack or not. If it does, the group is added to the current group and the stack is popped. If it doesn't, the stack is popped and added to the current group. This way, nested and unbalanced groups are properly handled. The current group is yielded when it is closed, and the last group in the string is yielded at the end.