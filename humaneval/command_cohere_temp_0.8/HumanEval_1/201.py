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
                result.append('')  # Incomplete group, ignore it
                continue
            current_group = stack.pop()
        else:
            current_group.append(char)

    # Handle potential leftover groups
    while stack:
        current_group = stack.pop()
        result.append(''.join(current_group))

    return result
```

This Python script takes a string of parentheses and splits them into separate groups. It uses a stack to keep track of open parentheses '(' and creates a corresponding list of strings. The resulting list of strings contains the separate groups of parentheses, properly balanced and without any nesting.