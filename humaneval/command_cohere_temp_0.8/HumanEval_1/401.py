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

The code uses a stack to keep track of nested paren groups and a current group tracker. It iterates through the characters of the input string, pushing groups onto the stack when encountering '(' and popping them when encountering ')'. When a ')>' is encountered, it is checked against the top of the stack to determine if the current group is closed. If so, it is yielded and the current group is set to the previous group. If not, the current group is yielded, and the stack is popped to continue parsing the nested group. This process effectively separates the nested paren groups into a list of individual groups.