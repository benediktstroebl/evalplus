```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    res = []
    for char in parentheses_string:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if stack:
                res.append(stack.pop(-1)
           pop()
                stack.pop()
           else:
            stack.append(0)
   else: pass
    return res

# Tests
def test_parse_nested_parens():
    test_str = "(()()) ((())) () ((())()())"
    assert parse_nested_parens(test_str) == [2, 3, 1, 3]
test_str = "((())())"
    assert parse_nested_parens(test_str) == []
test_str = "((()()))"
    assert parse_nested_parens(test_str) == []
test_str = "()()()"
    assert parse_nested_parens(test_str) == []
test_str = "((()))"
    assert parse_nested_parens(test_str) == [1]
test_str = "(())"
    assert parse_nested_parens(test_str) == []
test_str = "()()"
assert parse_nested_parens(test_str) == []
test_str = "))()"
assert parse_nested_parens(test_str) == []
test_str = "(()())"
    assert parse_nested_parens(test_str) == [2, 3, 1, 3]

# Run the tests when prompted. 
```