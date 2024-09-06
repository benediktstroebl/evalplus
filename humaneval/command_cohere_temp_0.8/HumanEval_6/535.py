```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for seg in s.split():
        level = seg.count('(') - seg.count(')')
        result.append(level)
    return result
```
The function processes the string segment by segment, counting the number of opening parentheses '(' and subtracting the number of closing parentheses ')' to arrive at the nesting level. This level is then appended to the `result` list. The entire list of nesting levels for all segments is returned, solving the problem.