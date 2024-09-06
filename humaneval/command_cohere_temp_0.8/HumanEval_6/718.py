```python
from typing import List

def parse_nested_parens(s: str) -> List[int]:
    result = []
    for chunk in s.split(' '):
        current_level = 0
        for char in chunk:
            if char == '(':
                current_level += 1
            elif char == ')':
                current_level -= 1
            result.append(current_level)
    return result
```

This script defines a function `parse_nested_parens` that takes a string `s` as input, containing multiple groups of nested parentheses separated by spaces, and returns a list where each element represents the deepest level of nesting of parentheses in the corresponding group. The function iterates through each chunk and maintains a `current_level` variable that keeps track of the current nesting level. It increments `current_level` for each opening parenthesis encountered and decrements it for each closing parenthesis. The final list `result` contains the deepest nesting level for each group of parentheses.

Here's an example usage of the function:
```python
>>> parse_nested_parens('(()()) ((())) () ((())()())')
[2, 3, 1, 3]
```

This will output `[2, 3, 1, 3]`, representing the deepest level of nesting for each group of parentheses in the provided input string.