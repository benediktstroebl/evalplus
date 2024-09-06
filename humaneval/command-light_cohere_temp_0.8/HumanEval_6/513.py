```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    """
    This function takes in a string of parenthesis groups and returns the deepest level of nesting for each group.

    Returns [] if the more than one level of nesting exists, otherwise the list is [].
    """
    return [i for i, _ in enumerate(parentheses_string.split(' ' '))] if '()' in parentheses_string else []

# Test cases
def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('()() () ((()))' == [1]
    assert parse_nested_parens('()(()) () ((()))') == []
    assert parse_nested_parens(')())' == []
    assert parse_nested_parens('() () ( )') == []
```