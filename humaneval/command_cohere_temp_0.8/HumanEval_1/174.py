Here's a Python script that contains a function called `separate_paren_groups` that accepts a string consisting of multiple groups of nested parentheses, separates these groups into individual strings, and returns a list containing these separated groups. This function disregards spaces within the input string.

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
                return []  # Unbalanced group, returning empty list as an indication of failure
            current_group = stack.pop()
        else:
            current_group.append(char)
    
    stack.append(current_group)
    return stack

# Example usage
test_string = "( ) (( )) (( )( ))"
print(separate_paren_groups(test_string))
```

This script uses a stack to keep track of opening parentheses until they are matched by a closing parenthesis. It then places the currently formed group onto the stack, effectively separating the groups. The final result is a list of strings, where each string corresponds to a separate group of parentheses. An example usage of this code is shown via a print statement in the test code provided alongside this script.