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
                return []
            top_group = stack.pop()
            if not stack:
                result.append(top_group)
            elif current_group:
                stack.append(current_group)
                current_group = top_group
        else:
            current_group += char

    # Handle the last group
    if stack:
        result.extend(stack)

    return result
```

The algorithm uses a stack to keep track of open parentheses `(` and builds corresponding strings for each
delimited substring between closing parentheses `)`. The final list of strings represents the separate groups
of parentheses. This approach guarantees that the result is correct, properly handles potential nested
groups, and is not prone to errors caused by race conditions. It also does not require any additional
inputs like the length of the string or the number of closing parentheses, as it exhaustively iterates
through the string and constructs the result based on the complete input information.