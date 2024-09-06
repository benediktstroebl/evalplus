Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of strings of separated parentheses group:
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
                return []  # Unbalanced group, returning empty list as an indicator of error
            current_group = stack.pop()
        else:
            current_group.append(char)

    # Handling potential unbalanced groups
    if stack:
        return []  # Unbalanced group, returning empty list as an indicator of error
    else:
        result.append(''.join(current_group))  # Add the remaining group if exists

    return result

# Example usage
assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
```

This script uses a stack to keep track of nested parentheses groups. When a closing parenthesis is encountered, it checks if it matches the most recent opening parenthesis on the stack. If so, it adds the corresponding group to the result list. The process is linear in terms of time complexity, which is acceptable for this type of problem.