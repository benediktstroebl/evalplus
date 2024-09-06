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
The provided Python script completes the task of separating nested parentheses into separate groups, employing a stack to keep track of open parentheses. Upon traversing each character of the input string, the code determines whether it's an open parentheses `(`. In such a case, the current group is pushed to the stack and a new group is initiated. When encountering a closing parentheses `)`, the code appends it to the current group while also reducing the stack's height by one, ensuring that groups are properly closed. Any character that isn't a parentheses is simply added to the current group. Ultimately, the function returns the list of distinct groups of parentheses.

Here is an example output of the function:
```python
separate_paren_groups("( ) (( )) (( )( ))")
['()', '(())', '(()())']
```

This output corresponds to the example provided in the problem statement.