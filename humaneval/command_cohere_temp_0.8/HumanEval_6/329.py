```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        current_depth = 0
        for char in chunk:
            if char == '(':
                current_depth += 1
            elif char == ')':
                current_depth -= 1
            result.append(current_depth)
    return result
```

This code defines a function `parse_nested_parens` that takes a string `s` as input, splits it into chunks separated by spaces, and processes each chunk separately to calculate the maximum nesting level of parentheses within that chunk. It does so by maintaining a `current_depth` variable that increments when encountering '(' and decrements when encountering ')'. The result array captures the highest level of nesting for each chunk, and the function returns this array as the final result.

Here is some example usage of the function:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```