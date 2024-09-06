```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, char in enumerate(s.split()):
        nest = 0
        level = 0
        j = 0
        while j < len(char):
            if char[j] == '(':
                nest += 1
                j += 1
            elif char[j] == ')':
                nest -= 1
                j += 1
                if nest == 0:
                    level = max(level, nest)
            else:
                j += 1
        result.append(level)
    return result
```

The `parse_nested_parens` function takes a string as input and splits it into characters. It then iterates over each character `char` and maintains a `nest` counter to keep track of the current nesting level for parentheses `'(''` and `')'`. It uses a `level` counter that is incremented when encountering a matching pair of parentheses and is reset if the nesting reaches zero. The function returns a list of these `level` values for each character, representing the deepest level of nesting of parentheses. 

Here is an example usage and test cases courtesy of `pytest`:
```python
def test_parse_nested_parens():
    assert parse_nested_parens('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert parse_nested_parens('()') == [0]
    assert parse_nested_parens('(((((()))))))' ) == [4]
    assert parse_nested_parens('(()') == []
    assert parse_nested_parens('())') == []
    assert parse_nested_parens('None') == []
```