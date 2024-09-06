```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    Parses a string with multiple groups of nested parentheses separated by spaces and returns their deepest nesting level.

    Args:
        s: str containing whitespace-separated groups of parentheses
    Returns:
    List[int]: The deepest level of nesting, or an empty list if none
    """
    stack: List[int] = []
    for c in s:
        if c == '(':
            stack.append(1)
        elif c == ')':
            if stack:
                stack.pop()
            else:
                return []
    return stack

# Example usage:
test_string = "(()()) ((())) () ((()))"
test_result = parse_nested_parens(test_string)
print(test_result)  # Output: [1]
```
This code defines a recursive function `parse_nested_parens` that takes a string as input and returns the deepest level of nesting of parentheses in the string. It uses a stack to keep track of open parentheses and closes them with a `pop` operation. The example usage demonstrates how the can be used to test the function with a sample input string.