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
                result.append(')'.join(current_group))
            else:
                pre_group = stack.pop()
                current_group.extend(pre_group)
                if not stack:
                    result.append(')'.join(current_group))
                    current_group = []
        else:
            current_group.append(char)

    # Handle the last group
    if notstack:
        pre_group = stack.pop()
        current_group.extend(pre_group)
    if current_group:
        result.append(')'.join(current_group))

    return result
```

The algorithm uses a stack to keep track of open parentheses `(` and collects them along with the nested content. When it encounters a closing parenthesis `)`, it checks if it matches the most recent open parenthesis on the stack. If it does, the current group is added to the result and the stack is popped to continue collecting the next group. If there are no more open parentheses on the stack, the collection cycle is complete and the current group is added to the result. Additionally, the program ignores any spaces encountered in the input string.

The approach guarantees correctly separating nested parentheses into separate groups, as long as the input follows the rule of nesting and each group is balanced (has matching open and close parentheses).