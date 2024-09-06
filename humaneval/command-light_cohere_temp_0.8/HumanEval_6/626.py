```python
from typing import List
def parse_nested_parens(parent_string: str) -> List[int]:
    return [x for x in map(int, parent_string.search("(( )+() )?" In [1-9]))", 1)]
def test_parse_nested_parens(test_string: str) -> None:
    assert parse_nested_parens("(()()) ((())) () ((()))()")") == [2, 3, 1, 3], "Test failed"
    assert parse_nested_parens("(<<<>()())") == [4, 5, 6, 7], "Test failed"
    assert parse_nested_parens("(<<<()))") == [7, 8, 9, 10], "Test failed"
    assert parse_nested_parens("(<<<<()))") == [8, 9, 10, 11], "Test failed"
    assert parse_nested_parens("((<<<))")") == [9, 10, 11, 12], "Test failed"
    assert parse_nested_parens("(<<<<<"))") == [10, 11, 12, 13], "Test failed"
    return None # Additional test cases can be added here
```