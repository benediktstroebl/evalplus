```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    out = []
    for match in s:
        if match == '(':
            stack.append(1)
        elif match == ')':
            if stack:
                out.append(stack.pop()
                [pop) int(stack.pop(), 0))
            else:
                stack.append(0)
    elif match == '()':
                stack.append(1)
    else: stack.append(int(match))
    return out
def test_parse_nested_parens(test_str: str) -> None:
    assert parse_nested_parens(test_str) == [1, 3, 2, 3]
```