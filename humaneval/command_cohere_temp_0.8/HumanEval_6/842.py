```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opened, closed in zip(*[iter(s.split())] * 2):
        count = opened.count(opened[0]) - closed.count(closed[0])
        result.append(count)
    return result
```
The function iterates over all pairs of opened and closed parentheses and for each calculates the difference between the number of opened and closed parentheses, which corresponds to the deepest level of nesting. This difference is appended to the result list.