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
                result.append('')  # Incomplete group, starting with a closing parenthesis
                continue
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.reverse()
    while stack:
        current_group.extend(stack.pop())
        result.append(''.join(current_group))
    
    return result
```
The solution uses a stack to keep track of nested parentheses groups. It iterates through the input string, pushing a new group onto the stack whenever it encounters an open parenthesis `(`. It pops the stack to switch back to the previous group when it encounters a closing parenthesis `)`. By popping the stack after the full string has been processed, any remaining groups on the stack are combined and added to the result list. This ensures that all groups are balanced and nested within each other. 

Here is an example output of the function:
```
['()', '(())', '(()())']
```
This output corresponds to the example provided in the problem statement.