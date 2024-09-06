```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function takes a string of nested parentheses and returns the deepest level of nesting.
    Example: This approach is to iterate through each character of the string, and based on its position and character, 
    determine the level of nesting.
    Args: 
    s: string of nested parentheses.
    Returns: a list of integers, where each integer corresponds to the deepest level of nesting found.
    """
This approach is to handle any nesting level. 
"""
    levels = []
    nesting = 0
    for char in s:
        if char == '(':
            nesting += 1
        elif char == ')':
            nesting -= 1
        else:
            levels.append(nesting)
    return levels
    """

Tests for this function:
```python
def test_parse_nested_parens(s: str) -> None:
    """
    Test string with different nesting levels
    """
    nested_levels = parse_nested_parens('(()) ((())) () ((()))()')
    assert nested_levels == [2, 3, 1, 3] is True
    nested_levels = parse_nested_parens(')())'
    assert nested_levels == [0] is True
    nested_levels = parse_nested_parens('()()()()())'
    assert nested_levels == [3] is True
```