```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    stack = []
    nest = []
    for c in s:
        if c == '(':
            stack.append(nest.append(0))
            nest = []
        elif c == ')':
            stack.pop()
            nested = stack.pop()
            nested[ nested[-1] ] += 1
            nest.append(nested)
        stack.append(0)
    return nest
```
The function takes an input string `s` and returns a list of counts of parentheses nested at different levels.