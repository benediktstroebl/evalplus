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
                temp = stack.pop()
                current_group.extend(temp)
                if not stack:
                    result.append(')'.join(current_group))
                    current_group = []
        else:
            current_group.append(char)

    # add the last group
    if not stack:
        result.append(')'.join(current_group))
    return result
```

The code uses a stack to keep track of nested parentheses groups. When a closing parenthesis is encountered, it is checked whether it matches the last opened parenthesis. If it does, the opened parenthesis is added to the current group. If it doesn't, the last group is added to the result, and the stack is popped to continue processing the current group. This process is repeated until all parentheses are processed. The resulting list of strings contains all the unique parenthesis groups, separated by nothing but parentheses and not nested within each other.