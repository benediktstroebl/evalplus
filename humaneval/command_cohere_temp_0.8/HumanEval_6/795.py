```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        nest = 0
        i = 0
        for char in segment:
            if char == '(':
                nest += 1
            else:
                nest -= 1
            i += 1
        result.append(nest)
    return result
```
The function splits the input string into segments using spaces as separators, and for each segment it counts the nesting level of parentheses. The maximum nesting level over all segments gives the deepest nesting for that group.