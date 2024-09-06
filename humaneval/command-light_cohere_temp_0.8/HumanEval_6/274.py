```python
def parse_nested_parens(paren_string: str) -> List[int]:
    stack = []
    opening = -1

    for i, char in enumerate(paren_string):
        if char == '(':
            opening += 1
        elif char == ')':
            opening -= 1
        else:
            if opening > 0:
                stack.append(opening)
                opening = -

    return stack

def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
```
The test_parse_nested_parens function checks if the function parse_nested_parens returns the right result.  It result is result is a list [2, 3, 1, 3] which corresponds to the deepest nesting of parentheses.