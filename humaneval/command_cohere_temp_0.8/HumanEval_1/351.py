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
                return ['Unbalanced parentheses!']
            current_group = stack.pop()
        else:
            current_group.append(char)

    if stack:
        return ['Unbalanced parentheses!']
    else:
        result.append(''.join(current_group))

    return result
```

The code uses a stack to keep track of opening parentheses '('. When a closing parenthesis ')' is encountered, the code checks if the stack is empty. If it's not empty, the top of the stack is popped and appended to the current group. The process is repeated until all the parentheses are processed.

The final result is a list of strings, where each string corresponds to a balanced group of parentheses found in the input string. The list of strings is then returned as the output.