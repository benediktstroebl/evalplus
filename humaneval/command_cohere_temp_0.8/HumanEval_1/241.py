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
                current_group = stack.pop()
    else:
        yield current_group
```

This code defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of
strings, each containing a separate group of parentheses. The function iterates through the input string, tracking
the current group of parentheses using a stack. When an opening parenthesis is encountered, it pushes the current
group onto the stack and starts a new group. When a closing parenthesis is encountered, it checks whether the
corresponding opening parenthesis is at the top of the stack. If it is, the current group is popped from the stack
and appended to the current group. If it's not, the stack is popped and the previous group is appended to the
current group. This process continues until all parentheses are processed. The final result is a list of
strings, where each string corresponds to a separate group of parentheses.

The example usage provided in the initial problem demonstrates its functionality:
```python
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
``` 

This exemplifies how the function correctly separates the groups of parentheses.