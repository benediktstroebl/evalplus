```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.split())] * 2):
        depth = 0
        curr = opening
        while curr != closing:
            if curr == '(':
                depth += 1
            elif curr == ')':
                depth -= 1
            curr = next(closing)
        result.append(depth)
    return result
```

The algorithm for parsing nested parentheses is a basic depth-first traversal. Given a string of parentheses, the function `parse_nested_parens` takes the string and returns a list of the deepest points of each nested block. 

Here is an example output of the function:
```python
parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```

This corresponds to the given example since the longest nested string is `(()())` with a depth of 2, followed by `((()))` with a depth of 3, then `()` with a depth of 1, and finally `((())()())` with a depth of 3.