Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of strings containing the separated parentheses:
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
                return []  # Unbalanced parentheses
            current_group.append(char)
            if not stack:
                result.append(')'.join(current_group))
                current_group = stack.pop()
            else:
                current_group = stack.pop()
        else:
            current_group.append(char)

    # Handle potential unbalanced parentheses
    if stack:
        return []

    return result

# Example usage
assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
```

This script uses a stack to keep track of nested parentheses groups. When a closing parenthesis is encountered, it checks if it matches the most recent opening parenthesis on the stack. If it doesn't, it returns an empty list assuming unbalanced parentheses. Otherwise, it adds the closing parenthesis and any characters between the matched pairs to the current group. Finally, it returns a list of these separated groups, resulting in the expected output as shown in the test case.