```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    result = []
    for char in parentheses_string:
        if char == "(":
            stack.append(1)
        else:
            if not stack or char == ")":
                result.append(len)
                stack.append(None)
            else:
                stack.append(stack.pop())
    maximize(result)
    return result
def test_parse_nested_parens():
    assert parse_nested_parens("(()()) ((())) () ((()))())" == [2, 3, 1, 3])
```