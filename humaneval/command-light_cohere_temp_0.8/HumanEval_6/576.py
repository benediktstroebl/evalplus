```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function parses a string with multiple groups of nested parentheses separated by spaces.

    Args:
        parent_string (str): The input string with nested parentheses.

    Returns: A list of the deepest level of nesting for each group of parentheses.

    Returns: list of nested integers:
    - The innermost parentheses are numbers 1, 2, and 3.
    """
    # Example:
    [1, 2, 3]
    """
    result = []
    stack = []
    nesting = 1
    for match in parent_string:
        if match == '(':
            stack.append(nesting)
        elif match == ')':
            if stack:
                stack.pop()
                result.append(nesting)
            nesting = 1
            stack = []
        else:
            stack.append(match)
    result.append(stack.pop())
   array = []
    return result
```

This code defines a function parse_nested_parens that parses a string of nested parentheses and returns a list of the deepest level of nesting for each group of parentheses.  It uses a technique of "Stacking" to track the nesting depth of each opening parenthesis, and uses a stack data structure to keep track of the opening parentheses that have been matched.  The function then checks for closing parentheses and adds the nesting depth to the result list.