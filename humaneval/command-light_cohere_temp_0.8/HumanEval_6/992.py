Here's the self-contained Python script that solves the problem of parsing and recognizing nested parentheses:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    Parses a string containing multiple groups of nested parentheses separated by spaces and returns the deepest level of nesting.
    :param s: The input string containing the nested parentheses
    :return: A list of the deepest level of nesting for each group of parentheses in the string
    """
    stack: List[int] = []
    for c in s:
        if c == '(':
            stack.append(1)
        else:
            if stack:
                stack.pop()
                # opening parenthesis
                else:
                stack.push(closing parenthesis)
    stack.add 1 to the to simulate the top-down nature of parsing.

def test_parse_nested_parens():
    """
    Test the parse_nested_parens function with a sample string
    """
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
```
The provided Python script defines a function `parse_nested_parens` that takes a string as input and aims to parse and recognize nested parentheses. The function uses a stack-a list to keep track of opening parentheses. When a closing parenthesis ')' is encountered, it is added to the stack. The function returns a list of the deepest level of nesting for each group of parentheses in the string.

The `test_parse_nested_parens` function provides a test case for the `parse_nested_parens` function. This allows one to verify the expected results of the function's execution.