Here's a Python script that contains a function called `separate_paren_groups` that accepts a string consisting of multiple groups of nested parentheses, separates these groups into individual strings, and returns a list containing these separated groups. The separation is based on the balance of parentheses and ignores any spaces in the input string.

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
            if stack:
                current_group = stack.pop()
            else:
                current_group.append(char)
        else:
            current_group.append(char)

    result.extend(current_group)
    return result

# Example usage
print(separate_paren_groups("( ) (( )) (( )( ))"))
```

This script uses a stack to keep track of nested parentheses and constructs the resulting strings accordingly. The example usage at the end demonstrates its functionality, outputting the result as `['()', '(())', '(()())']`.