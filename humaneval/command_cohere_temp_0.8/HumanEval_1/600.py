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
                return []  # unbalanced group, returning empty list as an indication of error
            current_group = stack.pop()
        else:
            current_group.append(char)

    # handle the last group
    if stack:
        result.extend(stack)
    else:
        result.append('()' if not current_group else current_group)

    return result
```

The algorithm uses a stack to keep track of open parentheses `(` and builds corresponding strings for each nested group. When it encounters a closing parenthesis `)`, it checks if the stack is empty, and if so, returns an empty list as an indication of an unbalanced group. Otherwise, it pops the top element of the stack to obtain the correct group that the closing parenthesis belongs to and then appends it to the result list.

The last group is handled correctly regardless if it is balanced or not, and any trailing parentheses are discarded. The solution ignores any spaces in the input string.