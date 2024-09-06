```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    result = []
    opening_parens = ['(', ')', '[]', '{', '[']
    closing_parens = [')', ')', ']', ']'
    
    for char in s:
        if char == ' ':
            stack.append(opening_parens.append(char)
        stack.append(closing_parens)
        result.append(len(stack)))
        stack = []
    
    return result
# Unit tests
def test_parse_nested_parens():
    assert parse_nested_parens('(()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('(,())')) == [1, 3]
    assert parse_nested_parens('((())')) == [1, 2]
    assert parse_nested_parens('(()()) (())() ()') == [2, 3, 1, 3]
    assert parse_nested_parens('(()()()) ((()))') == [3]
    assert parse_nested_parens('(()()  ))()') == []
    assert parse_nested_parens('() ()() ()() ()()') == []
    assert parse_nested_parens(') ()() ()() ()()') == []
    assert parse_nested_parens('{[][]}') == []
    assert parse_nested_parens('{} [()]') == []
    assert parse_nested_parens('{} [{}]') == []
    assert parse_nested_parens('[]') == []
    assert parse_nested_parens('() [()] ()') == []
```