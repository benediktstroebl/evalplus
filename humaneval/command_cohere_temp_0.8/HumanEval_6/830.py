Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result, depth = [], 0
    for segment in s.split():
        if segment == '()':
            depth += 1
        else:
            depth -= 1
        result.append(depth)
    return result
```
This script defines a single function `parse_nested_parens` which takes in a string as input and returns a list of the deepest levels of nesting of parentheses in each segment separated by spaces. It firstly counts the number of nested parens to calculate the depth and then subtracts when encountering a `()` to reflect the integrity of the segment.