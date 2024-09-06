```python
from typing import List


def parse_nested_parens(parentheses_string: str) -> List[int]:
    """
    This function is designed to parse and return the deepest level of nesting of parentheses from the input string.

    Parentheses are
    are nested following a certain format, with spaces separating each group.

    The function uses a List comprehension and a recursive descent approach to navigate through the string.

    Return a list containing the full nesting level of the deepest grouping of parentheses.
```

test_parse_nested_parens = [
    ("(()()) ((())) () ((())())"
    assert parse_nested_parens(test_string) == [2, 3, 1, 3],
    ("(+) ()(+) (+)"
    assert parse_nested_parens(test_string) == [2, 3],
    ("()()())"
    assert parse_nested_parens(test_string) == [1, 3],
    ("(()())()()"
    assert parse_nested_parens(test_string) == [2],
    ("()()())()"
    assert parse_nested_parens(test_string) == []
]
```
This script defines a function **`parse_nested_parens`** that takes a string of parentheses as input and uses a list comprehension and a recursive approach to navigate through the string and find the deepest level of nesting of parentheses. The test cases that demonstrate the expected output of the function for different input strings.