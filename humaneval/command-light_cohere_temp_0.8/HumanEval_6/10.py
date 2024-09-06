```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    ret = []
    for c in s:
        if c == '(':
            stack.append(1)
        elif c == ')':
            ret.append(stack.pop())
            stack.append(0)
   
        stack.append(c)
    return ret
def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((()))()')') == [2, 3, 1, 3]
    assert parse_nested_parens('()()) ((())())') == [2, 3]
    assert parse_nested_parens('(<<()))') == []
    assert parse_nested_parens(')()') == []
    assert parse_nested_parens('( )') == []
```
This code defines a function `parse_nested_parens` that takes a string as input and returns a list of integers representing the levels of nesting of parentheses in the string. Additionally, it includes a function `test_parse_nested_parens` to test the function's output for different inputs.