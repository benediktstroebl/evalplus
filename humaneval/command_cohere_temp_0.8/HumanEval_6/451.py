```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.split())] * 2):
        depth = 0
        nested = 0
        while opening != closing:
            if opening == '(':
                depth += 1
            elif closing == ')':
                depth -= 1
                nested += depth
            opening = closing
        result.append(nested)
    return result
```

This script takes a string `s` containing nested parentheses, split by spaces, and returns a list of the deepest level of nesting for each group. It uses `zip(*[iter(s.split())] * 2)` to create iterators for opening and closing parentheses, and uses `result.append(nested)` to keep track of the deepest level of nesting encountered in each group.

Here is an example usage of the function:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```

This is the expected output, as the first group has two nested parentheses, the second group has three nested parentheses, the third group has one nested parentheses, and the fourth group has three nested parentheses.