```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split():
        nesting = 0
        balance = 0
        for char in chunk:
            if char == '(':
                balance += 1
                nesting = max(nesting, balance)
            elif char == ')':
                balance -= 1
        result.append(nesting)
    return result
```

The `parse_nested_parens` function iterates over a string `s` split into space-separated chunks. It maintains a `nesting` counter that captures the current maximum depth of parentheses and a `balance` counter that tracks the current parentheses balance. As it iterates through each character `char` in a chunk, it increments the `balance` for opening parentheses `(` and decrements it for closing parentheses `)`. The `nesting` is updated with the maximum balance observed, ensuring correct depth tracking. The final result is a list of deepest nesting levels for each chunk, which corresponds to the input groups separated by spaces.

This approach allows the function to efficiently process nested parentheses in multiple groups and provide the deepest nesting level for each group.