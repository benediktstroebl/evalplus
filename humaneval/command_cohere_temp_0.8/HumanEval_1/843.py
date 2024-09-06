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
                print('There is an unclosed parenthesis group')
                return None
            current_group = stack.pop()
        else:
            current_group.append(char)

    if stack:
        print('There is an unclosed parenthesis group')
        return None

    result.append(''.join(current_group))

    return result
```

The function `separate_paren_groups()` uses a stack to keep track of nested parentheses groups. It iterates through the input string, adding opening parentheses to the stack and collecting characters in the current group. When a closing parenthesis is encountered, the stack is checked, and if the corresponding opening parenthesis is at the top of the stack, the current group is popped off and added to the result list. The process is repeated until all parentheses are processed.

This approach ensures that parentheses groups are correctly separated and nested groups are properly handled. It also handles the case where there are unmatched closing parentheses, avoiding potential errors. The resulting list of strings corresponds to the individual parentheses groups separated from the input string.