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
                return ['Invalid input! No opening paren to match this closing one.']
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack
```
The algorithm uses a stack to keep track of opening parentheses until the corresponding closing parenthesis is encountered. It initializes an empty list `result` to store the final list of separated groups. The loop iterates through each character of the input string, either pushing an empty list `current_group` onto the stack when an opening parenthesis is encountered or popping the top of the stack and assigning it to `current_group` when a closing parenthesis is encountered. Non-parentheses characters are appended to `current_group`.

After iterating through all characters, the top of the stack will be the last opening parenthesis group, which was not matched with a closing parenthesis. In this case, the algorithm will return an error message. Otherwise, it will return the list `result`, which contains all the separated groups of parentheses.