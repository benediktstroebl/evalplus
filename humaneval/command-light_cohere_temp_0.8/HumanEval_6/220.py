Here is a Python script that provides a self-contained function that solves the problem you have described. 

```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    This function parses a string containing multiple groups of nested parentheses separated by spaces.
    It returns a maximum nesting level of each parenthesis group in the input string.
    """
    return [ [map(lambda x: eval(x), s.split('()') for s in s.split('((()))' * ))
    )

def test_parse_nested_parens() -> None:
    test_str = "(()()) ((())) () ((()))"
    assert parse_nested_parens(test_str) == [2, 3, 1, 3]
    test_str = "(((((((())))))))))"
    assert parse_nested_parens(test_str) == [3, 3, 1, 3]

# run the function to test
test_parse_nested_parens()
```