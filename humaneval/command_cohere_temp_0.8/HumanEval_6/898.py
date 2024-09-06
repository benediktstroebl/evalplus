```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for token in s.split():
        level = 0
        nested = 0
        for c in token:
            if c == '(':
                nested += 1
            else:
                nested -= 1
            level = max(level, nested)
        result.append(level)
    return result
```

This script defines a single function `parse_nested_parens(s)` that takes in a string `s` containing multiple groups of nested parentheses separated by spaces, and returns a list of the deepest levels of nesting for each group. 

The function iterates through each token separated by spaces, and maintains a `level` counter that keeps track of the deepest level of nesting encountered so far. It initializes `nested` to zero before each iteration, and increments it for each `(` encountered, and decrements it for each `)` encountered. The `level` is updated with the maximum value between the current `nested` value and the previous `level`.

The list containing the maximum nesting levels for each token (and therefore for each group of parentheses) is then returned.

This solution works correctly for the given example and should pass the test cases.