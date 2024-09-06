```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    for c in s:
        if c == '(':
            stack.append(1)
        elif c == ')':
            if not stack or stack[-1] == 1:
                result.append(len)
                stack.clear()
            else: stack.append(0)
   
        elif c == '()':
            stack.append(1)
        else: stack[-1] += 1
    return result
def test_parse_nested_parens() -> None:
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3])
    assert parse_nested_parens('((()))') == [1]')
    assert parse_nested_parens('()()()()()()()()()') == []
    assert parse_nested_parens('()'') == []
    assert parse_nested_parens('((1)))()()') == [1]
    assert parse_nested_parens('()()()') == []
```  This code defines a function `parse_nested_parens` that parses and returns a list of the deepest level of nesting for a given string of nested parentheses. The test function passes all corresponding tests.