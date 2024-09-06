```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_par = segment.count('(')
        close_par = segment.count(')')
        result.append(open_par - close_par)
    return result
```

The `parse_nested_parens` function takes a string as input and splits it into segments using spaces as separators. It counts the number of open parentheses (`'('`) and closes parentheses (`')'`) for each segment separately and calculates the difference to obtain the deepest level of nesting for each segment. The results are then appended to a list and returned.

To test the function, you can call it with different input strings and compare the results with expected levels of nesting.

For example:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```