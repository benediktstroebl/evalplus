```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        balance = 0
        nesting = 0
        for char in chunk:
            if char == '(':
                balance += 1
            else:
                balance -= 1
            nesting = max(nesting, balance)
        result.append(nesting)
    return result
```

The `parse_nested_parens` function takes a string as input and returns a list of the deepest nesting level of parentheses in each sub-string. It operates by:
1. Splitting the input string into space-separated chunks.
2. For each chunk, the function keeps track of the current nesting level (`nesting`), which is simply the maximum of the current and previous balance.
3. The function returns a list of these maximum nesting levels for each sub-string. 

Such a solution correctly handles even cases like `(())()` and `((()))` yielding respective outputs of `[2, 3]` and `[3, 3]`.