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
                return []
            current_group += stack.pop()
        else:
            current_group += char
    
    return stack
```
The algorithm uses a stack to keep track of open parentheses '(' and pops them when it encounters a closing parenthesis ')' and nests the groups as it goes. This way, it is able to separate the groups and return a list of strings of each separate group, while also maintaining the correct grouping and balancing the parentheses.