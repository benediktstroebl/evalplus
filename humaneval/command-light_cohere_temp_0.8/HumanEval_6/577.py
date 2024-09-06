```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    """
    This function parses a string of nested parentheses and returns the deepest level of nesting.
    Test cases are provided.
    Test if parentheses string is empty or contains only spaces.
    Test if parentheses string: [(]) -> []
    """
    if not parenthesis_string:
        return []
    stack = []
    for parenthesis in parenthesis_string.group(1):
        if parenthesis == '(':
            stack.append(1)
        else:
            stack.append(3)
        stack.append(1)
    return stack
```
This code defines a function called `parse_nested_parens` that takes a string of parentheses as input and returns a list of integers representing the deepest level of nesting in the parentheses. It uses a stack to keep track of the current opening parenthesis and closing parenthesis. The function iterates over each character in the input string, and uses a set of tests to determine whether the character is a closing parenthesis or an opening parenthesis.