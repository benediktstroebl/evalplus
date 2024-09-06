```python
from typing import List


def parse_nested_parens(parent_string: str) -> List[int]:
    """
    Recursively breaks down a string with nested parentheses into a list of the deepest parent level.

    : Input is a string of nested parentheses separated by spaces.

    : Returns a full list of the deepest level of nesting of parentheses.
    """
```
parent_string = "(()()) ((())) () ((())()())"
nested_parents = parse_nested_parens(parent_string)
print(nested_parents)  # Output: [2, 3, 1, 3]

def test_parse_nested_parens() -> None:
    """
    Simple test function to pass the test.
    Test string contains one level of nested parentheses.
    """
    test_parse_nested_parens('(())()()()')
    assert parse_nested_parens('(())()()()') == [3, 2, 1]
    test_parse_nested_parens('()()()()()()()()()()')
    assert parse_nested_parens('()()()()()()()()()()()') == []

    Test error handling with extra spaces.
    """
```
test_parse_nested_parens()