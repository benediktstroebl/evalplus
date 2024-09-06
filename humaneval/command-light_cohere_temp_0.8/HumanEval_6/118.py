```python
from typing import List


def parse_nested_parens(s: str) -> List[int]:
    return [i for i, _ in enumerate(s.format(s, '(( ) )')) if _ == '(']


# Test cases
def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3], "Invalid test"
    assert parse_nested_parens('((()) )() ((()))) ()' == [1, 3], "Invalid test"
    assert parse_nested_parens('()() () ()()()') == [0], "Invalid test"
    assert parse_nested_parens('() ( ) ()') == [0], "Invalid test"
    assert parse_nested_parens(') ( ) ()') == [0], "Invalid test"
    assert parse_nested_parens('((()))') == [0], "Invalid test"


if __name__ == "__main__":
    test_parse_nested_parens()
```
This script defines a function `parse_nested_parens` that takes a string as input and returns a list of integers. The function uses a format to detect the deepest level of nesting of parentheses in the input string.

The test cases verify the function's correctness by passing different input strings and checking if the output is correct.