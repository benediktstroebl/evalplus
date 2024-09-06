```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for token in s.split():
        level = 0
        nesting = 0
        for c in token:
            if c == '(':
                nesting += 1
            else:
                nesting -= 1
            level = max(nesting, level)
        result.append(level)
    return result
```

The `parse_nested_parens` function takes a string as input and returns a list of the deepest level of nesting of parentheses for each group separated by spaces.

The script includes a test example that validates the function correctly solves the problem:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
``` 

This test case demonstrates the function's ability to parse different levels of nesting within each group correctly.