```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for segment in s.split():
        level = 0
        nesting_level = 0
        for char in segment:
            if char == '(':
                nesting_level += 1
            elif char == ')':
                nesting_level -= 1
            else:
                pass
            level = max(level, nesting_level)
        result.append(level)
    return result
```

This code defines a function `parse_nested_parens` that takes a string as input and returns a list of deepest nesting levels of parentheses in each segment separated by spaces. For example, the input `'(()()) ((())) () ((())()())'`will produce the output `[2, 3, 1, 3]`. The algorithm achieves this by:
- Splitting the input string into segments using spaces.
- Initializing a variable `level` to keep track of the maximum depth of parentheses encountered so far.
- Similarly, a `nesting_level` is initialized to keep track of the current nesting level of parentheses.
- Iterating through each character in the segment:
  - If the character is `(`, it increases the `nesting_level`. 
  - If the character is `)`, it decreases the `nesting_level`. 
  - When the `nesting_level` becomes zero, the `level` is updated to its current value.
- Appending the maximum level of nesting for each segment to the result list.

The code ensures that even with confusing edge cases like nested parentheses in the input, it safely calculates the deepest level of nesting for each group without any error.