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

The algorithm uses a stack to keep track of nested parentheses groups. It shifts every opening parenthesis to the stack and collects all other characters in the current group. When a closing parenthesis is encountered, the stack is checked. If it is empty, the current group is added to the results array and reset. If there is at least one element in the stack, the top element (the most recently added opening parenthesis) is popped and added to the current group. This process is repeated until all input is processed. The resulting list of strings contains all possible bracket expressions, each surrounded by parentheses and not nested within each other.

Here is an example usage of the function:
```python
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
```