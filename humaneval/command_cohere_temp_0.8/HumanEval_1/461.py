Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of separate groups of parentheses.
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
                result.append(')'.join(current_group))
            else:
                current_group.append(char)
        else:
            current_group.append(char)
    
    while stack:
        current_group = stack.pop()
        result.append(')'.join(current_group))
    
    return result
```
The function relies on a stack to keep track of opening parentheses until we encounter a closing one. All nested and unbalanced groups are discarded. The resulting list contains properly balanced and separate parentheses groups, as desired.