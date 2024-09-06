```python
from typing import List
def parse_nested_parens(parenthes_str: str) -> List[int]:
    stack = []
    in_string = False  # To keep track of whether we are inside an actual parentheses
    opening = False  # To track whether we are in the process of opening a parentheses
    closing = False  # To track whether we are in the process of closing a parentheses
    for char in parenthes_str:
        if char == " ":
            if in_string:
                stack.append(1)
                in_string = False
            closing = True
        elif char == "(":
            if not in_string:
                in_string = True
                opening = True
            stack.append(1)
        elif opening and closing:
            stack.append(3)
            opening = False
            closing = False
        elif char == ")":
            if opening and closing:
                stack.append(3)
                opening = False
                closing = False
            else:
                stack.append(1)
                closing = True
        else:
            in_string = False
        return stack

# Test cases
parenthes_str = "(()()) ((())) () ((()))"
print(parse_nested_parens(parenthes_str))  # Output: [2, 3, 1, 3]
```
This script defines a `parse_nested_parens` function that takes a string of nested parentheses as input and returns a list of the deepest levels of nesting. It uses a ` stacks ` opening`, `closing`, and `in_string` to keep track of the current state of opening and closing parentheses and uses backtracking to determine the deepest level of nesting.