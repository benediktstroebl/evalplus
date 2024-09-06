```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    forOpening, i, maxLevel = 0, 0, 0
    for char in s:
        if char == '(':
            forOpening += 1
            i += 1
            if forOpening > maxLevel:
                maxLevel = forOpening
        else:
            forOpening -= 1
        result.append(maxLevel)
    return result
```

The algorithm utilizes a state-machine approach to keep track of '(' characters and increment the maximum nesting level whenever a '(' character is encountered. When a ')' character is encountered, the function resets the current nesting level to 0. The maximum achieved nesting level is recorded in the `result` list, which is later returned.