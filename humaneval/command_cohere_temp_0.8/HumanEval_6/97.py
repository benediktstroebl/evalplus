```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        count = 0
        nesting = 0
        nonlocal result
        for char in chunk:
            if char == '(':
                nesting += 1
                if nesting > count:
                    count = nesting
            else:
                nesting -= 1
        result.append(count)
    return result
```
The function processes each chunk (separated by a space) separately and keeps track of the current nesting level `count` and current nesting level `nesting`. Increasing the nesting level counts as increasing the level, whereas decreasing the nesting level acts as a placeholder and contributes to the count of how many nestings were able to go into this level.