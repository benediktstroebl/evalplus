```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    output = []
    for char in parentheses_string:
        if char == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                output.append(char)
            else:
                stack.append(len)
    else:
                    stack.append(len[0])
    output.append(char)
    return output
def test_parse_nested_parens() -> None:
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3])
```