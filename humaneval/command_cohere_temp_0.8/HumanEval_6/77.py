```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for i, char in enumerate(s.split()):
        nesting = 0
        level = 0
        start = 0
        for c in char:
            if c == '(':
                nesting += 1
                if nesting == 1:
                    start = i+1
                else:
                    level = max(level, nesting)
            elif c == ')':
                nesting -= 1
        result.append(level)
    return result
```

The approach involves:
- Splitting the input string by spaces to separate individual groups of parentheses.
- Iterating through each character of each group, tracking the nesting level of parentheses.
- Maintaining a `start` index to relate the deepest nesting level to the appropriate group.
- Storing the deepest nesting level for each group in a list as the output.