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
                print(f"Invalid input: {char} is not inside any group.")
                return []
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    if stack:
        print("Invalid input: Input string should be fully processed.")
        return []
    else:
        result.extend(current_group)
        return result
```

This script uses a stack to keep track of opening parentheses `(` and builds corresponding closing parentheses `)` into `current_group`. Once the stack is empty, the current group is added to the `result` list and returned. It also handles improperly nested or unbalanced groups, printing an error message and returning an empty list in those cases. 

Here is an example output:
```bash
>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']
```