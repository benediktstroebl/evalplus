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
                return ['Unbalanced parentheses in input!']
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack
```
The code uses a stack to keep track of opening parentheses '(', and creates a corresponding list for each open parentheses group. It also handles improperly nested or unbalanced groups. Unfortunately, there is no built-in function in Python to directly solve this problem, as it would be too magic to be practically applicable to more complex cases. Let me know if you would like me to explain how the code works in detail!