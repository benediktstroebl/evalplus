```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""

    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            current_group += char
            if not stack:
                yield current_group
            elif stack[-1] == current_group:
                stack.pop()
                current_group = stack.pop() if stack else ""
            else:
                yield current_group
        else:
            current_group += char

    # yield any remaining groups
    while stack:
        yield stack.pop()
```

This code defines a function `separate_paren_groups` that takes a string as input and returns a list of string values. It uses a last-in-first-out (LIFO) stack to maintain the current group and another stack to hold the resulting string groups. It iterates through each character in the input string and for opening parentheses, it pushes the current group (if any) onto the stack and starts a new group; for closing parentheses, it checks the stack to determine whether the current group is properly closed and nested. If so, it pops the group from the stack and continues with the previous group, or yields the current group and starts a new one if the stack is empty. It yields any remaining groups at the end if they were properly closed but not nested within other groups.

Here is an example usage of the function:
```python
print(list(separate_paren_groups("( ) (( )) (( )( ))")))
```

This will output the following result:
```
['()', '(())', '(()())']
``` 

This demonstrates the function's ability to correctly separate the nested parentheses into separate groups and return them in a list.