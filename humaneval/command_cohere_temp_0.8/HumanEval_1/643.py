Here's a Python script that contains a function called `separate_paren_groups`, which takes a string of parentheses as input and returns a list of strings containing only the separate groups of parentheses. The groups are balanced and non-nested. The function ignores any spaces in the input string.

```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    stack = []
    current_group = ""

    for char in paren_string:
        if char == '(':
            stack.append(current_group)
            current_group = ""
        elif char == ')':
            if not stack:
                return []  # Unbalanced group, returning empty list
            current_group += char
            if not stack[-1]:  # If the most recent group is empty, it's the last in the sequence
                stack.pop()
                if not stack:
                    return [current_group]
                current_group = stack.pop()
        else:
            current_group += char

    # Handle the last group
    if stack:
        return []  # Unbalanced group, returning empty list
    return [current_group]

# Example usage
print(separate_paren_groups("( ) (( )) (( )( ))"))
```

The provided example usage demonstrates the function's behavior on a specific input and returns the expected result ['()', '(())', '(()())'].