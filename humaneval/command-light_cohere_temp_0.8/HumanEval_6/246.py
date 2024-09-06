```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    """
    This function is designed to parse a string of nested parentheses.
    Parameters:
    string to be parsed is passed in as s.
    Returns: a list of the deepest level of nesting of parentheses in the string.
    """

    test cases:
    """
    assert parse_nested_parens("()() ((()()))) == [2, 3, 1, 3],
    "Error in parsing the parentheses"

    assert parse_nested_parens("(()()))") == [1],
    "Error in parsing the parentheses"

    assert parse_nested_parens("(()())") == [1],
    "Error in parsing the parentheses"

    assert parse_nested_parens("()()())") == [],
    "Error in parsing the parentheses"

    assert parse_nested_parens("((((()))))))") == [4, 3, 2],
    "Error in parsing the parentheses"

    return [0] # Test an invalid string
```