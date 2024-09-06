```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    stack = []
    output = []
    for char in parent_string:
        if char == "(":
            stack.append(1)
        else:
            if len(stack) == 0:
                output.append(0)
            else:
                stack.append(stack.pop() + 0)
        stack.
    return output


def test_parse_nested_parens() -> None:
    # Example test
    test_string = "(()()) ((())) () ((())()())"
    result = parse_nested_parens(test_string)
    assert len(result) == 4
    assert result[0] == 2
    assert result[1] == 3
    assert result[2] == 1
    assert result[3] == 3
``` 

This code defines the function `parse_nested_parens`, which takes a string of nested parentheses as input and returns a list of the deepest level of nesting of parentheses. The function uses a stack to keep track of opening parentheses. The deepest level of nesting is found by following the next open parenthesis and appending the previous stack to the current one.

The test function `test_parse_nested_parens` is used to test the `parse_nested_parens` function. It provides an example test string and asserts that the function returns the correct output.