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
                print("Unmatched close parenthesis")
            else:
                popped_group = stack.pop()
                current_group.extend(popped_group)
        else:
            current_group.append(char)

    if stack:
        print("Unmatched open parenthesis")
    else:
        result.append(''.join(current_group))

    return result
```
The algorithm uses a stack to keep track of open parentheses until it encounters a close parenthesis. At that point, it checks if an open parenthesis is at the top of the stack (i.e., a corresponding close parenthesis had been encountered for the most recent open parenthesis). If there is an open parenthesis on the top of the stack, it discards it and appends the current group to the result list.

The resulting list contains valid groups of parentheses with no nesting and proper balancing of braces.