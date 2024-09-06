```python
from typing import List
def parse_nested_parens(parenthes_string: str) -> List[int]:
    """
    This function takes a string with multiple groups of nested parentheses separated by spaces as input.
    It returns the particular level of nesting of parentheses.
    It uses a nested list comprehension to parse the string.
    The example usage: [('(())', 2), ('(()())', 3), ('(()())()', 1), ('(()())()()', 3)]
    """
    return [match[1] for match in zip((puple[0] for purle in parentheses) for parentheses in purle)]
def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((())()())')') == [2, 3, 1, 3]
    assert parse_nested_parens('(()()))') == []
    assert parse_nested_parens('())') == []
    assert parse_nested_parens('()()())') == []
    assert parse_nested_parens(') (((()))))') == []
```
This Python script defines a function `parse_nested_parens` that parses and returns the deepest level of nesting of parentheses in a given string. The `test_parse_nested_parens` function contains several assertions that validate the output of the `parse_nested_parens` function for different inputs.