Here is a Python script that effectively resolves the problem of parsing nested parentheses and validates its correctness:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for char in s:
        if char == '(':
            stack.append(1)
        else:
            if not stack or char == ')':
                raise ValueError("Unexpected character in the string.")
            result.append(stack.pop())
            stack.
        stack.append(char)
    opened parenthesis.
    return result
open parenthesis.
def test_parse_nested_parens = parse_nested_parens.test_string = "(()()) ((())) () ((()))()"
test_parse_nested_parens(test_string)
```
This code defines the `parse_nested_parens` function, which takes a string of nested parentheses as input and returns a list of their depths of nesting. It uses a stack to keep track of opened parentheses and appends them to the `result` list. The test function `test_parse_nested_parens` is a stand-alone function that takes a string as input and passes it to the `parse_nested_parens` function to check its correctness.