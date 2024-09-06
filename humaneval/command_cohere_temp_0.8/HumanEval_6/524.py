Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result, levels = [], 0
    for i, char in enumerate(s):
        if char == '(':
            levels += 1
            result.append(levels)
        elif char == ')':
            levels -= 1
    return result
```

This script can be imported as a module and called directly, providing an immediate evaluation of the function.

The `parse_nested_parens` function takes a string `s` as input, which contains multiple groups of nested parentheses separated by spaces. It uses an intelligent technique to monitor the nesting level while traversing the string, increasing the count when encountering '(' and decreasing it when encountering ')', thereby providing the required result.