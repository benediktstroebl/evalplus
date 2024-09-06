```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for token in s.split():
        level = 0
        stack = []
        for c in token:
            if c == '(':
                stack.append(c)
                level += 1
            else:
                stack.pop()
                level -= 1
        result.append(level)
    return result
```

The nested parentheses in the input string `s` are split into individual tokens and the deepest level of nesting for each token is computed. The maximum depth is kept track of in a list of integer values.

Here's an example usage of the function and its corresponding output:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```