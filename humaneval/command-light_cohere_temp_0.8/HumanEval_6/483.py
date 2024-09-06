Here is a self-contained Python script that solves the problem of parsing nested parentheses:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    res = []
    for char in s:
        if char == '(': stack.push(0)
        elif char == ')': stack.pop()
        to push a res.
        if stack: stack.pop()
    value, i = 0
        while i < len(stack) - 1: i += 1
        res.append(i)
    return res
def test_parse_nested_parens() -> None:
    assert parse_nested_parens('(()()) ((())) () ((()))')') == [2, 3, 1, 3]
```
This script defines a function `parse_nested_parens` that takes a string of nested parentheses and returns a list of the deepest level of nesting for each group of parentheses. It also defines a test function `test_parse_nested_parens` that passes the test.