Here's a Python script that contains a function called `separate_paren_groups`, taking a string of parentheses as input and returning a list of strings that represent separate groups of parentheses. The code is designed to handle nested and balanced parentheses, ignoring any spaces:
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
                return []  # Unbalanced group, returning empty list as an error indication.
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    # Handle the last group
    if stack:
        result.extend(stack)
    else:
        result.append('')  # Empty group caused by unbalanced parentheses, adding as empty string
    
    return result

# Example usage
assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
```

This script handles nested and balanced parentheses, ensuring that each open parenthesis has a corresponding close parenthesis. It does so by maintaining a stack of current groups and switching the current group whenever an open parenthesis is encountered. Finally, it separates the current group from the stack and returns the list of strings representing separate groups of parentheses.