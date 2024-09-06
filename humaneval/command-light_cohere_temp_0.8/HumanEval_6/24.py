```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    Parses a string of nested parentheses into a list of their depths.

    Args:
        s (str): A string of parentheses.
    Returns: list of depths of the deepest nesting of each group of parentheses.
    """
    The test suite:
    Test that this function returns the right output for the given input.
    """
    This test_cases = [
        "(()())((()))()",
        "()((()))",
        "((()()))",
        "()()()",
        "()()()()()",
        "()()(())",
        "((()())())"
    ]
    assert parse_nested_parens("(()())((()))()") == [2, 3, 1, 3]
    assert parse_nested_parens("()((()))") == [1]
    assert parse_nested_parens("((()()))") == [2]
    assert parse_nested_parens("()()()") == [0]
    assert parse_nested_parens("()()()()()") == []
    assert parse_nested_parens("()()(())") == [1]
    assert parse_nested_parens("((())())") == [2]
    assert parse_nested_parens("((()())()") == [3]
    assert parse_nested_parens("()()()()()()()") == []
```
The test suite ensures the correct output for various input scenarios.