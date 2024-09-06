```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        level = 0
        curr = 0
        for c in chunk:
            if c == '(':
                curr += 1
            else:
                curr -= 1
            level = max(level, curr)
        result.append(level)
    return result
```

The code processes each group of parentheses separately and uses a stack-like algorithm to keep track of the nesting level. It iterates through each character in the chunk, increments if the character is `(`, and decrements if it is `)`. It keeps track of the maximum nesting level encountered by incrementing a level variable whenever the counter is `> 0`. The list of maximum nesting levels for each group is returned.