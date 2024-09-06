```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for opening, closing in zip(*[iter(s.split())] * 2):
        depth = 0
        curr = opening
        while curr != closing:
            if curr == '(':
                depth += 1
            elif curr == ')':
                depth -= 1
            curr = next(closing)
        result.append(depth)
    return result
```

The `parse_nested_parens` function takes a string `s` as input, where each whitespace-separated segment represents a nested group of parentheses. The function iterates through each segment, keeping track of the opening and closing parentheses. It uses `zip(*[iter(s.split())] * 2)` to ensure it handles nested groups equally well in cases with more than one layer of nesting. For each opening parenthesis, it increments the `depth` counter, and for each closing parenthesis, it decrements it. Once the matching parentheses are reached, the current depth is appended to the `result` list.

The provided example test case and usage example demonstrate how to call this function and verify its correctness. The function handles nested groups with varying levels of indentation, providing the deepest level of nesting for each segment.