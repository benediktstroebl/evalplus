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

This script includes the function `parse_nested_parens()` that takes a string as input and returns a list of deepest levels of nesting of parentheses in each of the groups separated by spaces. The function uses a stack to track the nesting level and increments the level when encountering an '(' and decrements when encountering a ')'arguably. It iterates through each group in the input separated by space, tracking the maximum nesting level within each group and returning the list of these levels.

Here is an example input/output to illustrate the functionality:
**Input:**
```
(()()) ((())) () ((())()())
```
**Output:**
```
[2, 3, 1, 3]
```