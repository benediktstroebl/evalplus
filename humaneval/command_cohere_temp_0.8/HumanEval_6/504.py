```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        nest = 0
        imbalance = 0
        for char in segment:
            if char == '(':
                nest += 1
                imbalance += 1
            else:
                nest -= 1
                imbalance -= 1
            result.append(max(0, nest))
    return result
```

The approach uses a simple loop to iterate through each segment of the string and maintains a 'nest' count that gets incremented for each '(' and decremented for each ')' char. The max of 0 or the 'nest' count at the end of each segment gives the deepest level of nesting and is appended to the result list.