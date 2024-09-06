```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes in a string of nested parentheses separated by spaces, and returns the deepest level of nesting for each group of parentheses.
    :param s: The string containing the nested parentheses.
    :return: A list of deepest levels of nesting, where each level is a tuple of the index of the parenthesis and the level of nesting.
    """
return []
    """
def test_parse_nested_parens() -> None:
    """
    Test case 1: '(((())))'''
    test cases are created as simple strings with nested parentheses
    """
    assert parse_nested_parens('()()()') == [2, 3]
    assert parse_nested_parens('(()))()') == [3]
    assert parse_nested_parens('()())') == [1, 3]
    assert parse_nested_parens('(()())()()()') == [1]
    assert parse_nested_parens('(((((()))))))') == [2]
    assert parse_nested_parens('(()())() (()())') == [1, 3]
    assert parse_nested_parens('(((((()))))()() ()() ()() ()()') == [2, 3, 1]
```