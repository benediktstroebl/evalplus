```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    stack.append([0])
    levels = 3
    paren_string = '(()()) ((())) () ((())()())'
    while s:
        p = s.strip()
        if p == '(':
            stack.append(levels)
            stack.append([])
        levels += 3
            s = s[len(p)+1:]
        elif p == ')':
            if len(stack) == 0:
                raise ValueError("Unexpected closing parenthesis")
            stack.pop()
            stack[-1] = stack.append([])
            stack.append([])
            levels -= 2
            s = s[len(p)+1:]
        else:
            stack.append(p)
        s = s[len(p)+1:]
    return stack

# Test code
def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('(())) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('(()) () ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('(((((((()))))))))))') == []
    assert parse_nested_parens('()()') == []
    assert parse_nested_parens('()') == []
    assert parse_nested_parens('(((((((())))))))))))') == []
```
The code defines a function `parse_nested_parens` that takes a string of nested parentheses as input and returns a list of corresponding integer levels of the deepest nesting. The function uses a method of parsing using a stack to keep track of open parentheses. The test code then validates the expected outputs of the `parse_nested_parens` function for various input strings.