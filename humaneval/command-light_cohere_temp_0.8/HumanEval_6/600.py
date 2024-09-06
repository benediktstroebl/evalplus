```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[str] = []
    in_string = False
    output: List[int] = []
    for c in s:
        if c in ['(', ')']:
            if in_string:
                stack.append(c)
                in_string = not in_string
            else:
                in_string = True
        elif in_string:
            stack.append(c)
        else:
            if c == ' ':
                stack.append(' ')
            else:
                in_string = True
            output.append(stack.pop()
    stack)
    return output
def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('()') == []
    assert parse_nested_parens('(((((((()))))))))))))))' == [4, 4]
    assert parse_nested_parens('(,()())') == []
```