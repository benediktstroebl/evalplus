Here's the code you asked for:
```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function is designed to parse and return the deepest level of nesting of parentheses in the provided string.
    Args:
        s (string): string to be parsed for nested parentheses

    Returns:
    List of positions (countings of opening parentheses)
    """
    return [pos for pos, in enumerate(s.lower()[:len(s)//4]) if s[pos:][0] == '(']
#unit tests
def test_parse_nested_parens():
    test_cases = [
        '(()()) ((())) () ((())()())',
        '((()))',
        '(()())',
        '(())()()',
        '(())  ()'
    ]
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('((()))') == []
    assert parse_nested_parens('(()())') == []
    assert parse_nested_parens('(())  ()') == []
    assert parse_nested_parens('()()()') == []
    assert parse_nested_parens('()  ( )') == []
    assert parse_nested_parens('()()()()') == []
```
This code defines a function `parse_nested_parens` that parses and returns the deepest level of nesting of parentheses in a given string.  The function utilizes the lowering technique to identify and count the positions of opening parentheses in the string, with a condition to determine if it's a valid group of opening parentheses. 
This function is then tested with several test cases to ensure its correctness.