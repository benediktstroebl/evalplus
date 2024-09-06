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
                return []  # Unbalanced group, returning empty list as error value
            current_group += char
            if not stack[-1]:  # If the top of the stack is empty
                stack.pop()
            else:
                current_group = ""
        else:
            current_group += char
    
    return stack if not current_group else stack + [current_group]
```

The provided solution utilizes a stack to properly separate the nested groups of parentheses. It maintains a current group as it iterates through the input string, pushing the current group onto the stack whenever it encounters an open parenthesis '('. It also handles the case when it encounters a closing parenthesis ')' without an open one on the top of the stack, which indicates the end of a group. The final result is a list of strings corresponding to the nested groups of parentheses, properly separated.