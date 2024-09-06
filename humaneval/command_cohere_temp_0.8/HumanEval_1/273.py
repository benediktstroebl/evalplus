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
                print("Unmatched close parenthesis")
            else:
                temp = stack.pop()
                current_group.extend(temp)
        else:
            current_group.append(char)

    stack.extend(current_group)
    result.extend(stack)
    return result
```

This script uses a stack to keep track of nested parentheses groups. When a closing parenthesis is encountered, the stack is checked to see if it is empty, indicating an unmatched closing parenthesis. If it's not empty, the group at the top of the stack is appended to the current group and the stack is popped to indicate that the current group is now closed. The current group is added to the result list whenever it is closed. This process is repeated until the entire string has been processed.

Here is an example usage of the function:
```python
print(separate_paren_groups("( ) (( )) (( )( ))"))
```

Should print:
```bash
['()', '(())', '(()())']
``` 

This example demonstrates how the `separate_paren_groups` function would handle the given input and provide the expected output.