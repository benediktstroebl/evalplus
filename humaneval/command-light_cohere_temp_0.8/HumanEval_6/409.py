```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack = []
    result = []
    for char in parenthes_string:
        if char == ')':
            if not empty:
                stack.append(len)
                else:
                    stack.append(len[-1])
            empty = True
        elif char == '(':
            stack.append(1)
        else:
            stack.append(char)
    result.append(stack.pop())
    open()
    return result
def test_parse_nested_parens() -> None:
    # Example test string
    test_str = "(()()) ((())) () ((())()())"
    expected = [2, 3, 1, 3]
    result = parse_nested_parens(test_str)
    assert result == expected
    return result
``` 
The provided code defines a function `parse_nested_parens` that parses and returns a list of the deepest levels of nesting of parentheses in a string. The function uses a `stack` to keep track of the nesting levels of the parentheses encountered in the string.

The `test_parse_nested_parens` function serves as a test for the `parse_nested_parens` function. It provides an example test string and asserts that the result of calling `parse_nested_parens` with the test string is equal to the expected nested parentheses levels.