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
            else:
                stack[-1] += top_group
        else:
            current_group += char

    return result
```

The code uses a stack to keep track of nested parentheses groups. When it encounters a closing parent, it checks whether the stack is empty. If so, there are unbalanced parentheses, and the function returns an empty list. If there are elements in the stack, it removes the top element, completes the current group, and appends it to the list if the stack is empty or appends the top element to the previous group if not. The resulting list of strings contains all the separate parentheses groups without nested or unbalanced groups.