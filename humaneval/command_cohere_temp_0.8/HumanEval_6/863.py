```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for nested_parens in s.split():
        current_level = 0
        for char in nested_parens:
            if char == '(':
                current_level += 1
            elif char == ')':
                current_level -= 1
            result.append(current_level)
    return result
```

The `parse_nested_parens` function takes a string as input and splits it into several parts using spaces as separators. Each part represents a different group of parentheses. Then, for each group, the function counts the number of '(' and ')' characters to calculate the current level of nesting. The result is a list that contains the deepest level of nesting for each group.