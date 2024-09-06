```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    stack = []
    output = []
    for char in parenthes_string:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if not stack or stack[-1] != 1:
                raise ValueError("Unexpected character after )")
            output.append(stack.pop(-1)[::-1]
            stack.append(0)
        else:
            stack.append(char)
    return output
def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('((()))') == [3]
    assert parse_nested_parens('()()())()()()()()()()()()()) == []
    assert parse_nested_parens('() (())') == []
```