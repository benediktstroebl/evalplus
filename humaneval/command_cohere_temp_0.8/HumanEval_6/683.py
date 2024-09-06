```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_depth in map(count_bracket_depth, s.split()):
        result.append(bracket_depth)
    return result

def count_bracket_depth(s: str) -> int:
    nesting_level = 0
    for char in s:
        if char == '(':
            nesting_level += 1
        elif char == ')':
            nesting_level -= 1
    return nesting_level
```
This script divides the input string s into multiple segments separated by spaces, and feeds each segment to the count_bracket_depth function to calculate the deepest level of nesting of parentheses in the corresponding segment. The result list accumulates these values.