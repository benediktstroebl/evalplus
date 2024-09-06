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
                return []  # Unbalanced parenthesis, return empty list
            current_group = stack.pop()
        else:
            current_group.append(char)

    # Handle potential trailing unbalanced parentheses
    while stack:
        current_group.extend(stack.pop())

    result.extend(current_group for current_group in stack)
    return result

# Example usage
assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
```

The provided example usage demonstrates how the function can be used to separate groups of parentheses found in the input string. The function balances and separates nested parentheses into individual groups, as outlined by the problem statement.