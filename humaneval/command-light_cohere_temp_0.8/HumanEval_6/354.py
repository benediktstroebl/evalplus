```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    # Initialize empty list to store results
    result = []
    stack = []

    # Iterate through each character in the string
    for char in parent_string:
        # If it's a close bracket ')'
        if char == ')':
            # If the stack is empty, add the current character to the result list
            if stack == []:
                result.append(char)
            # Otherwise, pop a character from the stack and continue to the next character
            stack.append(char)
        # If the stack has elements, push the current character to it and continue with the next character
        stack.append(char)
        # If the stack is empty again, this is the end of the group, so add the empty list to the result list
        stack = []

    return result
```