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
                result.append('')
            elif not stack[-1]:
                result.append('')
            else:
                stack.pop()
                current_group.append(char)
                if not stack:
                    result.append(''.join(current_group))
        elif char != ' ':
            current_group.append(char)

    # Handle the last group
    if notstack:
        result.append(''.join(current_group))

    return result
```
This approach uses a stack to keep track of nested parentheses groups. It iterates through the input string, pushing a
        new group onto the stack whenever it encounters an open parenthesis `(`. When it encounters a close parenthesis
        `)`, it checks if the stack is empty. If the stack is empty, it appends an empty string to the result list, implying
        an unbalanced parenthesis group. If there is a group on the stack, it pops it and appends the characters between the
        last open and close parenthesis to the current group. The process continues until the entire string has been
        processed. The final result contains a list of separate parentheses groups.