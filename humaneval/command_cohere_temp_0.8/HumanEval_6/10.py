```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        depth = 0
        balance = 0
        nesting_level = 0
        for char in segment:
            if char == '(':
                balance += 1
            elif char == ')':
                balance -= 1
                nesting_level = max(nesting_level, balance)
            if balance < 0:
                break
        result.append(nesting_level)
    return result
```

The approach involves splitting the input string into segments using spaces as separators. For each segment, the function maintains a `depth` variable to keep track of the current balance of parentheses and a `nesting_level` variable to track the maximum depth reached during the life span of a particular group of parentheses. The function initializes `nesting_level` and `balance` to zero and iterates through each character in the segment. 

If the character is a left parenthesis `(`, the `balance` is increased. If the character is a right parenthesis `)`, the `balance` is decreased and the `nesting_level` is updated to the maximum of the current `nesting_level` and `balance`. The function keeps tracking the maximum nesting level until it reaches the end of the string or a segment with a negative balance (i.e., an unmatched opening parenthesis). At the end of each segment, the result list is appended with the final nesting level for that segment.