```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    output = []
    for i, char in enumerate(s):
        if char == "(":
            stack.append(1)
        elif char == ")":
            if not stack:
                stack.append(0)  # empty parenthesis
            else:
                stack.pop()
        if stack:
                    output.append(stack.pop()
                    maximum) number of pairs in the parentheses to form the correct tree.
# Test cases
def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((()))')') == [2, 3, 1, 3]
    assert parse_nested_parens('(abc)(123))') == []
    assert parse_nested_parens('()') == []
    assert parse_nested_parens('((()))') == []
```