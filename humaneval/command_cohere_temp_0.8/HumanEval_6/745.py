```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        nest = 0
        for c in chunk:
            if c == '(':
                nest += 1
            else:
                nest -= 1
        result.append(nest)
    return result
```
The code splits the input string into chunks using spaces as separators, and then iterates through each chunk to count the number of '(' characters to determine the deepest level of nesting of parentheses. The result is a list of these deepest levels for each corresponding chunk. 

The following tests are included to verify correct functionality of the `parse_nested_parens` function:
```python
def test_parse_nested_parens():
    # Happy path
    assert parse_nested_parens("(()()) ((())) () ((())()())") == [2, 3, 1, 3]
    assert parse_nested_parens("()") == [0]
    assert parse_nested_parens("(((((()()))))))") == [4]

    # Edge cases
    assert parse_nested_parens("") == []
    assert parse_nested_parens("Some text with no parentheses.") == []
    assert parse_nested_parens("(()") == [1]
    assert parse_nested_parens("())") == [1]
    assert parse_nested_parens("(()())") == [2]
```