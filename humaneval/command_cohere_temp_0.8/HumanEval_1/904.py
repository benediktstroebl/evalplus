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

The algorithm uses a stack to keep track of nested parentheses groups. When a closing parenthesis is encountered, the group is appended to the current group if the stack is empty, indicating the end of a group. If there are elements in the stack, the last group is popped and appended to the current group. The procedure is repeated until all parentheses are processed. The resulting current_group is then added to the result list.

This approach ensures that parentheses groups are correctly separated and nested within each other, resulting in a list of balanced groups.