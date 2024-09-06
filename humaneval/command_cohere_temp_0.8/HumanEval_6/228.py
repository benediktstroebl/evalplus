```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    forOpening, forClosing = 0, 0
    for char in s:
        if char == '(':
            forOpening += 1
        elif char == ')':
            forClosing += 1
        if forOpening > forClosing:
            result.append(forOpening)
            forOpening = 0
            forClosing = 0
    if forOpening > forClosing:
        result.append(forOpening)
    return result
```

The algorithm counts openings and closings directly after reading the input string. When an imbalance is detected, it resets the counters. The final count is stored in the result list. The expected output for the provided test case is: `[2, 3, 1, 3]`.