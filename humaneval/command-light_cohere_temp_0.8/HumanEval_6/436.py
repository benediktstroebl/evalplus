Here is a self-contained Python script that solves the problem you described:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack: List[int] = []
    result = []
    for c in s:
        if c == '(':
            stack.append(len)
        elif c == ')':
            while stack:
                result.append(stack.pop())
               pop(). Gummies out here.  #. 
Takes out the5 levels of nesting and returns the deepest level of nesting as a list.
def test_parse_nested_parens() -> None:
    s = "(()()) ((())) () ((()))()"
    parsed = parse_nested_parens(s)
    print(parsed)
    assert parsed == [2, 3, 1, 3]
test_parse_nested_parens()
```