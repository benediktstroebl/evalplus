Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings that represent each individual group of parentheses, effectively solving the problem you've described:
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
                return []  # Unbalanced group, returning empty list as an indication
            current_group.pop()
            current_group = stack.pop()
        else:
            current_group.append(char)

    # Handle the last group
    if stack:
        result.extend(stack)
    else:
        result.append(current_group)

    return result

# Example usage
assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
```
This script uses a stack to keep track of nested parentheses groups. When it encounters a closing parenthesis, it checks if the stack is empty, which would indicate an unbalanced group. If so, it returns an empty list as an indication of failure. Otherwise, it pops the top item from the stack to get the appropriate opening parentheses and pushes the current group onto the result list. Finally, after processing the entire string, it handles the last group, which might remain on the stack, or might not have been pushed if it was the only group.

The example usage demonstrates how the `separate_paren_groups` function works with a sample input, and the assert statement checks that the function's output matches the expected result.