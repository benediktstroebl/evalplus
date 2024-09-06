```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    """
    This function takes a string of nested parentheses separated by spaces as input and returns a list of the deepest level parentheses found.
    The approach: Try to match the longest valid parent string and increment the counter.
    If a valid parent string, the inner and outer parentheses are considered as the same level and the counter is incremented.

    If a longest valid parent string is found, the list of parentheses at that level is returned.
    """
    test cases:
    ```python
    assert parse_nested_parens('(()()) ((())) () ((()))')')[2] == 3
    assert parse_nested_parens('()() ((())) () ((()))')')[3] == 1
    assert parse_nested_parens('( )() ((())) () () ((()))')')[3] == 1
    assert parse_nested_parens('()() ((())) () ())) ()' == [2, 3, 1]
    assert parse_nested_parens('( )() ((())) ())) ()' == [3, 1]
    ```