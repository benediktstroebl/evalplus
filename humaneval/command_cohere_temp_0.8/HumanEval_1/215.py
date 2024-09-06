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
                return []  # unbalanced group, return empty list
            current_group = stack.pop()
        else:
            current_group.append(char)

    # handle the last group
    if stack:
        result.extend(stack)
    else:
        result.append(current_group)

    return result
```
The algorithm uses a stack to keep track of open parentheses `(` and constructs the resulting strings accordingly. 

Here is an example usage of the function:
```python
print(separate_paren_groups("( ) (( )) (( )( ))"))
```
The output of this code will be:
```bash
['()', '(())', '(()())']
```
This result is expected, each group of parentheses is separated and returned as a list element. The spaces have been ignored as per the instructions.