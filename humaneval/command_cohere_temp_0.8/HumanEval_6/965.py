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
The `parse_nested_parens` function takes a string as input and splits it into segments using spaces as separators. For each segment, it counts the number of `(` and `)` characters to calculate the deepest level of nesting of parentheses. The result is a list of these nesting levels for each segment.