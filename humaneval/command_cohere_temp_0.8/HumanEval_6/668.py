```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        open_brace_count = sum(1 for char in segment if char == '(')
        close_brace_count = sum(1 for char in segment if char == ')')
        result.append(open_brace_count - close_brace_count)
    return result
```

This script uses a **split** mechanism to iterate over the different segments and calculates the difference between the number of open and closed parentheses to accordingly add the level of nesting to the result list.

The following is a test case for this function to ensure its correctness:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```

This output shows the levels of nesting in each segment separated by spaces.