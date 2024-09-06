Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of strings of separated parentheses group:
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
            if not stack:
                return []
            current_group += char
            stack.pop()
        else:
            current_group += char
    
    return stack + [current_group]
```

This script includes a function that accepts a string of parentheses and returns a list of strings representing individual parentheses groups. The internal `stack` variable stores the currently opened brackets. When a closing bracket `)` is encountered, the corresponding opened bracket is popped from the stack to ensure proper balancing. If the stack is empty at any point, it indicates an unbalanced bracket, and the function returns an empty list. The final output list contains each separate group, including any trailing parentheses.