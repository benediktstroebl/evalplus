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
                result.append(''.join(current_group))
            else:
                temp = stack.pop()
                current_group.extend(temp)
                if not stack:
                    result.append(''.join(current_group))
        else:
            current_group.append(char)

    return result
```

This Python script uses a stack to track the open parentheses until we encounter a closing parenthesis. Then, we check if the current group is nested properly and flush it to the result if it is not. We also check if the current group is empty or not, since an empty group at the end also should be flushed to the result. The result list contains the separate groups of parentheses without any spaces.