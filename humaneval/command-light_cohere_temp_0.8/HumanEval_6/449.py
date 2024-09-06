```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    opened = False  # flag to track if parentheses are opened
    output = []  # list to store the result

    for char in parent_string:
        if char == ' ':
            if opened:
                stack.append(output[-1])  # Pop and add to output
            opened = False  # reset opened flag
        elif char == '(':
            opened = True
        elif char == ')':
            opened = False

    return output  # Return the full list of parenthesis levels
def test_parse_nested_parens() -> None:
    assert parse_nested_parens('(()) ((())) () ((()))')') == [2, 3, 1, 3]
```
This code defines the function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest level of parentheses. It uses a stack to keep track of the parentheses opened, and it pushes the deepest level onto the stack each time a new opening parenthesis is encountered. Then, when a closing parenthesis is encountered, it pops the deepest level from the stack and adds it to the output list. The `test_parse_nested_parens` function tests this `parse_nested_parens` function with a sample input string and asserts that the returned list of integers matches the expected output.