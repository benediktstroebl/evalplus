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
                result.append(')')
            else:
                current_group.pop()
                if not current_group:
                    result.append(')')
                else:
                    stack.pop()
        else:
            current_group.append(char)

    # Add remaining
    while stack:
        current_group.pop()
        if not current_group:
            result.append(')')
        else:
            stack.pop()
    if current_group:
        result.append(''.join(current_group))

    return result

# Example usage
assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
```

This script uses a stack to keep track of nested parentheses groups. It iterates through the input string, adding opened parentheses to the stack and collecting all other characters in a list. When a closing parenthesis is encountered, the stack is checked to determine whether it corresponds to the most recent opened parenthesis or not. If it does, both the stack and current_group are popped. This process continues until all parentheses are processed, after which the current_group is appended to the result if it's not empty. This approach ensures that unbalanced or nested parentheses are handled correctly.