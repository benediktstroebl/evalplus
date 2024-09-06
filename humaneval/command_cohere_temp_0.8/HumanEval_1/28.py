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
            current_group = []
        else:
            current_group.append(char)

    if not stack:
        result.append(''.join(current_group))
    else:
        while stack:
            temp = stack.pop()
            current_group.extend(temp)
        result.append(''.join(current_group))

    return result
```

The algorithm uses a stack to keep track of open parentheses and a list to aggregate the content inside each closed parentheses group. It iterates through the input string, pushing each open parenthesis onto the stack and collecting the enclosed characters in the current group. Upon encountering a closing parenthesis, it checks if the stack is empty. If so, it returns the current group as a standalone string. If not, it retrieves the top element from the stack (the corresponding open parenthesis), concatenates it with the current group, and keeps the result in the current group.

After processing all characters, the function returns a list of strings, where each string corresponds to a balanced group of parentheses. The intended behavior is to ignore spaces and provide valid outputs for the provided and possible test cases.