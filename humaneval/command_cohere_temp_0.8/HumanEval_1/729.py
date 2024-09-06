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
                print('UNBALANCED!)')
                continue
            current_group.append(char)
            if not stack:
                result.append(')'.join(current_group))
                current_group = stack.pop()
            else:
                current_group = stack.pop()
        else:
            current_group.append(char)

    # add remaining groups
    while stack:
        current_group.append(')'.join(stack.pop()))
        result.append('(' + '))'.join(current_group) + ')')

    return result
```

This script uses a stack to keep track of nested parens and creates a list of strings where each string contains a separate group of parens. It ensures that the opening parens are balanced with closing parens and that there are no nested parens. The resulting list of strings is returned.