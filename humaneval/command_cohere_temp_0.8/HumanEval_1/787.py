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
                    result.append((').extend(current_group)')
                elif char != ')':
                    stack.append(current_group)
                    current_group = []
        else:
            current_group.append(char)

    if current_group:
        result.append(')'.join(current_group))

    return result
```

The algorithm uses a stack to keep track of nested parentheses groups. When an open parentheses `(` is encountered, it adds an empty string to the stack. When a closing parentheses `)` is encountered, the algorithm checks if the stack is empty. If it is, it appends the `)` to the `result` list, assuming it closed the outermost group. If the stack is not empty, the algorithm pops a string from the stack, appends it to the current group, and checks if the stack is empty again. If it is not, it pushes the current group onto the stack and resets it. If the current group hasn't been appended to the result yet, it will be after popping the last group from the stack.

The resulting list of strings corresponds to the nested groups of parentheses in the input string, excluding any spacing.

This approach allows the function to correctly separate the nested parentheses groups from the input string and return them as a list of strings.