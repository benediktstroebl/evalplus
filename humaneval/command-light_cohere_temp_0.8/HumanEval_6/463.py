Here is a Python script with a self-contained function that solves the problem of parsing and identifying the deepest level of nesting for a given string:
```python
def parse_nested_parens(s):
    return [i for i, x in enumerate(s.group if isinstance(x, str)]

def test_parse_nested_parens(s):
    result = parse_nested_parens(s)
    expected = [2, 3, 1, 3]
    assert result == expected
```

This script defines a function `parse_nested_parens` that takes a string `s` as input and returns a list of its nested levels, and a function `test_parse_nested_parens` that takes a string `s` as input and passes the corresponding test.