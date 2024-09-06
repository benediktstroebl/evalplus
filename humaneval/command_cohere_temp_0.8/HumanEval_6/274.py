Here's a Python script with a self-contained function that solves the problem using a greedy algorithm:
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result, depth = [], 0
    for char in s:
        if char == '(':
            depth += 1
            result.append(depth)
        elif char == ')':
            depth -= 1
    return result
```

The `parse_nested_parens` function iterates through the input string `s`. When it encounters an open parentheses `'('` it increases the `depth` counter. When it encounters a closing parentheses `')'`, it decreases the `depth` counter. The result list is used to store the maximum depth of nesting encountered during each group and finally returns it. 

This solution works efficiently and is relatively straightforward to understand. It uses a greedy approach to increment and decrement the counter based on the immediate context, which gives the correct result for the given problem.