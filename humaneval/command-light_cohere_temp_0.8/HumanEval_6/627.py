```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    stack = []
    open_parens = []
    closing_parens = []

    for char in parentheses_string:
        if char == ')':
            if closing_parens:
                stack.append(closing_parens.pop()
                open_parens)
                closing_parens = []
        elif char == '(':
            open_parens.append(char)
            closing_parens.append(char)
        stack.append(open_parens)

    return stack
def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((()))()') == [2, 3, 1, 3])
```
The function `parse_nested_parens` parses a string of nested parentheses, and the `test_parse_nested_parens` function tests if the function returns the right output for a given string.