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
                result.append('')  # Incomplete group, bail
            else:
                temp = stack.pop()
                current_group.extend(temp)
                if not stack:
                    result.append(''.join(current_group))
                    current_group = []
        else:
            current_group.append(char)

    while stack:
        temp = stack.pop()
        current_group.extend(temp)

    if current_group:
        result.append(''.join(current_group))

    return result
```

The algorithm uses a stack to keep track of open parentheses `(` and builds resulting strings on the fly.

It shifts the current group onto the stack when it encounters an open parenthesis `(`. This indicates that a new
group starts. When it encounters a close parenthesis `)`, it checks if the stack is empty. If it isn't, the algorithm
pops the last group off the stack, appends it to the current group, and checks if the stack is empty again. This
process effectively combines the two groups and continues until the last group is closed.

If the stack is empty when a close parenthesis is encountered, that indicates an unbalanced group, and the algorithm
appends an empty string to the result. This is consistent with the specification that unbalanced groups are ignored.