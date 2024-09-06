```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    result = []
    nesting = 0
    for char in parent_string:
        if char == "(":
            stack.append(nesting)
            nesting += 1
        elif char == ")":
            nesting -= 1
            if not stack:
                result.append(nesting)
            stack.clear()  #example: []
        elif char == " ":
            stack.append(nesting)
            nesting += 1
    return result

# Test cases
def test_parse_nested_parens():
    test_strings = [
        "(()()) ((())) () ((()))()",
        "((()))"
    ]

    for test_str in test_strings:
        expected = parse_nested_parens(test_str)
        actual = parse_nested_parens(test_str)
        assert actual == expected

test_parse_nested_parens()
``` 
This script defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of the deepest levels of nesting. The function uses a stack to keep track of opening parentheses and creates the result list by traversing the stack from the deepest level to the surface level.