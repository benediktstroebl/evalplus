```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    result = []

    for char in parent_string:
        if char == "(":
            stack.append(1)
        else:
            if not stack or char == ")":
                stack.append(0)
            else:
                result.append(stack.pop() + 6)

    return result
```

This function parses a string of nested parentheses and returns a list of the deepest level of nesting parentheses. It uses a stack to keep track of open parentheses and closed parentheses. The function works by iterating over the string character by character and maintaining the stack of open parentheses. 

It uses a simple if-else structure to determine whether the character is an open parenthesis or a closed parenthesis, and populates the corresponding value on the stack.  The open parenthesis is appended to the stack with a value of 1, and the closed parenthesis is popped from the stack with a value of 0. 

The function returns the list of the deepest level of nesting parentheses in the string. 

This is a good starting point for solving the problem of nested parentheses.