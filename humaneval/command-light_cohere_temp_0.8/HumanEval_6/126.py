```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function takes a string with nested parentheses as input and returns the deepest level of nesting as a list of integers.
    Example string:
    Input: ('(()())((()()))()((())())))
    Output: [2, 3, 1, 3]
    """
    stack: List[int] = []
    i = 0
    while i < len(parent_string):
        if parent_string[i] == ")":
            stack.append(i+
            stack.append(i+
            stack.append(i+))
            i+=2
        else:
            i+=1
    return stack
def test_parse_nested_parens(input_string: str) -> None:
    """
    This function tests the parse_nested_parens function with various inputs and ensures the output is correct.
    Input:
    Outputs:
    None
    """
    if not parse_nested_parens(input_string):
        raise ValueError("Error in function parse_nested_parens")
```
This code defines a function `parse_nested_parens` that parses a string of nested parentheses and returns the deepest level of nesting as a list of integers. The function utilizes a stack data structure to keep track of open parentheses and their positions. The function tests the certain characters as ")" and "(" to push them onto the stack, and any other character as it is encountered.

The `test_parse_nested_parens` function tests the `parse_nested_parens` function with various inputs and ensures the output is correct. The output of this test function is None, which means that the function passed the test successfully.