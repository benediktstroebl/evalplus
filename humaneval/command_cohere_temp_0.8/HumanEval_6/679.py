```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        nest = 0
        level = 0
        stack = []
        for c in segment:
            if c == '(':
                stack.append(c)
                nest += 1
            else:
                nest -= 1
                stack.pop()
            level = max(level, nest)
        result.append(level)
    return result
```

The `parse_nested_parens` function takes a string as input and returns a list of the maximum nesting level of parentheses in each segment. It splits the string into segments based on spaces, and then keeps track of the current nesting level `nest` as it iterates through each character in a segment. When it encounters an open parenthesis `(`, the nesting level increases, and when it encounters a close parenthesis `)`, the nesting level decreases. The maximum nesting level `level` encountered within a segment is stored in the result list.