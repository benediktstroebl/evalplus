```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        nest = 0
        for c in chunk:
            if c == '(':
                nest += 1
            else:
                nest -= 1
        result.append(nest)
    return result
```

This script splits the input string into spaces and then loops over these parts, effectively simulating a stack for each part. It increments the 'nest' counter whenever it sees an '(' and decrements it whenever it sees a ')', giving the resultating nesting count for each corresponding part.

Such a solution intuitively mirrors the 'recursive' thought process one would employ when manually solving the problem.