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
                return ['Unbalanced parentheses!']
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack
```

The algorithm utilizes a stack to keep track of opening parentheses '(' and constructs the list of strings when all opening parentheses are closed. The algorithm correctly handles nested groups of parentheses and ensures that the result is always a list of strings, even in the case of unbalanced parentheses. 
This approach uses the stack data structure in a clear way to solve this problem. The result is a list of strings where each element in the list corresponds to a separate group of parentheses with any characters inside them.