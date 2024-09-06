```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    forOpening, i = 0, 0
    for char in s:
        if char == '(':
            forOpening += 1
            i = 0
        elif char == ')':
            forOpening -= 1
            i += 1
        if forOpening > i:
            result.append(forOpening)
    return result
```

The provided Python script defines a function `parse_nested_parens` that takes a string `s` containing multiple groups of nested parentheses separated by spaces as input. It iterates through each open parenthesis `(`, incrementing a counter `forOpening` while also keeping track of the current index `i`. When a closing parenthesis `)` is encountered, `forOpening` is decremented, and `i` is incremented. The difference between `forOpening` and `i` at each closing parenthesis indicates the deepest level of nesting for the current group. This information is appended to a list `result`. The script provides a straightforward solution to the problem of finding the maximum nesting level of parentheses within each group in the provided string.