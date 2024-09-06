Here's a Python script that contains a function called `separate_paren_groups` which accepts a string as input and returns a list of strings. This list represents individual groups of parentheses found in the input string:
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
                print('Unmatched closing parenthesis')
                return []
            current_group = stack.pop()
        else:
            current_group.append(char)

    if stack:
        print('Unmatched opening parenthesis')
    else:
        result.extend(current_group)

    return result

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack to keep track of nested parentheses groups. When a closing parenthesis `)` is encountered, the code checks if it matches the most recent opening parenthesis `(` on the stack. If so, the group is added to the results. If not, it indicates an unbalanced group of parentheses. 

The resulting list of strings, representing the balanced groups of parentheses, is returned by the function.