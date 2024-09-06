```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    opening = 0
    closing = 0
    output = []
    for char in parentheses_string:
        if char == "(":
            opening += 1
        stack.append(opening)
        closing = 0
        output.append(stack.pop()
   
        if char == ")":
            closing += 1
        stack.append(closing)
    if closing == opening:
            stack.pop()
            output.append(stack.pop()
    if closing != opening:
            output.append(opening)
            opening = 0
            closing = 0
    return output
def test_parse_nested_parens():
    assert parse_nested_parens('(()) ((())) () ((())()())') == [2, 3, 1, 3]',
    assert parse_nested_parens('(())) () () ((())()())') == [1, 3, 2],
    assert parse_nested_parens('()()()()()()()()()()') == [2, 3, 1],
    assert parse_nested_parens('(()))()()()()()()()()()()()()') == [],
    assert parse_nested_parens('()((()))') == []
```