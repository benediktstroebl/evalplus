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

    # Adding the last group
    if not stack:
        result.append(')'.join(current_group))
    elif current_group:
        temp = stack.pop()
        current_group.extend(temp)
        result.append(')'.join(current_group))

    return result
```

The algorithm uses a stack to keep track of nested parentheses groups. It initializes an empty list to store the overall results. Then it loops through the characters of the input string one by one. When encountering an open parenthesis `(`, it pushes the current group onto the stack and initializes a new empty group. When encountering a closing parenthesis `)`, it checks if the stack is empty. If true, it appends the closing parenthesis to the result as there is an extra closing parenthesis. If false, it retrieves the top item from the stack, which is the previous group, and appends its contents to the current group. This goes on until the end of the string, with the final groups getting appended to the result list.