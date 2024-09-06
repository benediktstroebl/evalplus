```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for bracket_group in s.split():
        count = 0
        opening_brackets = 1
        for char in bracket_group:
            if char == '(':
                opening_brackets += 1
            elif char == ')':
                opening_brackets -= 1
            count = max(count, opening_brackets)
        result.append(count)
    return result
```

This code defines a function `parse_nested_parens` that takes a string `s` containing multiple groups of nested parentheses separated by spaces, and returns a list where each element represents the deepest level of nesting of parentheses in its corresponding group.

The algorithm works by:
1. Splitting the input string into individual groups of parentheses using the `split()` method, which assumes spaces as separators.
2. Initializing a `count` variable to zero for each group.
3. Iterating through each character in a group. If the character is `'(''`, it increments the `opening_brackets` count, and vice versa. The `count` variable is then updated to the maximum value between its current value and `opening_brackets`.
4. The maximum nesting count is appended to the `result` list.

This approach efficiently determines the maximum nesting level of parentheses within each group of the input string.