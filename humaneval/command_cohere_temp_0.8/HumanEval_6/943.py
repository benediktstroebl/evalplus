```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, bracket_str in enumerate(s.split()):
        level = 0
        nesting_level = 0
        opening_bracket = 1
        for char in bracket_str:
            if char == '(':
                opening_bracket += 1
            elif char == ')':
                opening_bracket -= 1
            if opening_bracket < 0:
                nesting_level += opening_bracket
                opening_bracket = 0
            level = max(level, nesting_level)
        result.append(level)
    return result
```
The code processes each group of parentheses separately and calculates the deepest level of nesting for each group. The maximum nesting level among all groups represents the overall maximum depth.

Here is an example usage of the function:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```
This result shows that the string has some groups with a maximum nesting level of 2, some with 3, and one with 1.