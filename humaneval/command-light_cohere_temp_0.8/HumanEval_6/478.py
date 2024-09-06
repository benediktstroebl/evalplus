```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    Recursively parses and returns the deepest level of nesting of parentheses in the string.
    :param s: str
    return: List[int], list of integer values in the deepest nesting of parentheses
    """
    stack: List[int] = []
    open: List[str] = []
    close: List[str] = []

    for char in s:
        if char == "(":
            open.append(char)
        else:
            close.append(char)
             # Continue to check for matching open and close parentheses
            if open and close:
                stack.append(int(open[0]) + int(close[0])))
            open, close = open[1:], close[1:]
            
    if open:
        stack.append(int(open[0]))
    return stack

# Unit tests
def test_parse_nested_parens():
    test_str = "(()()) ((())) () ((())()())"
    result = parse_nested_parens(test_str)
    assert len(result) == 2
    assert result[0] == 2
    assert result[1] == 3
    test_str = "(((()()()())))()"
    result = parse_nested_parens(test_str)
    assert len(result) == 3
    assert result[0] == 4
    assert result[1] == 3
    assert result[2] == 4
    test_str = "(((((((()))))))))"
    result = parse_nested_parens(test_str)
    assert len(result) == 5
    assert result[0] == 10
    assert result[1] == 10
    assert result[2] == 20
    assert result[3] == 20
    assert result[4] == 20

# Run the tests when run directly on the script
test_parse_nested_parens()
```
This script defines a function `parse_nested_parens` that parses and returns the deepest level of nesting for a given string of parentheses. It also includes several unit tests to verify the correctness of the function. The function uses a stack to keep track of open and closed parentheses, and it uses a "depth-first" approach to traverse the string and build the stack of integers that represent the nesting levels.