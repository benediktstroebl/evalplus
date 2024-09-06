```python
from typing import List
def parse_nested_parens(parentheses_string: str) -> List[int]:
    return [i for i, match in enumerate(re.parse(parentheses_string, nested=True), match is not None]
def test_parse_nested_parens() -> None:
    assert parse_nested_parens("(()()) ((())) () ((())()())")") == [2, 3, 1, 3]
    assert parse_nested_parens("( barney ))") == []
    assert parse_nested_parens("( )")) == []
    assert parse_nested_parens("(( foo ))") == []
    assert parse_nested_parens("( foo ((bar)) )")) == [2, 4, 3]
```
This code defines a function `parse_nested_parens` that parses and returns the deepest level of nesting for a given string of parentheses. It then has several tests, asserting that the function works correctly for various inputs.