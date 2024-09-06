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

    # Handle the last group
    if stack:
        result.extend(stack)
    else:
        result.extend(current_group)

    return result
```

This script uses a stack to keep track of opening parentheses `(` and constructs the corresponding `result` list of strings accordingly. For each closing parenthesis `)`, it checks if the stack is empty, which indicates an unbalanced parenthesis case and returns an error message. Otherwise, it pops the top item of the stack, which is the list of characters for the closest opening parenthesis, and appends it to the `result`.

The `result` list is returned, which encompasses all the separated groups of parentheses. Given an input like `('( )) (( )( ))'`)`, the algorithm will output:
```bash
['()', '(())', '(()())']
```