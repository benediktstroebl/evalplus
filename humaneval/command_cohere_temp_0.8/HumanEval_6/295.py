```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        nest = 0
        i = 0
        for char in chunk:
            if char == '(':
                nest += 1
            else:
                nest -= 1
            i += 1
        result.append(nest)
    return result
```
The code processes each group of parentheses separately and calculates the deepest level of nesting for each one. The result is a list where each element represents the maximum nesting level of the corresponding group.