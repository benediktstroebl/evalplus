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
                result.append(')')
            else:
                temp_group = stack.pop()
                current_group.extend(temp_group)
                if not stack:
                    result.append(')'.join(current_group))
                    current_group = []
        else:
            current_group.append(char)

    # Add the last group
    if current_group:
        result.append(')'.join(current_group))

    return result
```

The algorithm uses a stack to keep track of open parentheses and a list to collect the current string of parentheses. When it encounters a closing parenthesis, it checks if it has an open one on the stack, and if so, it adds the string collected to the result and pops the open parenthesis from the stack. If there are no more open parentheses, the collected string is added to the result. This approach allows to separate the parentheses into separate groups without considering the nesting and balance of parenthesis groups.